#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_ROOT="${1:-/tmp/zdeck-build}"
EXPORT_ROOT="${2:-${ROOT}/builds}"
PROJECT_JSON="${ROOT}/project.json"

read_json() {
    python3 -c "import json; print(json.load(open('${PROJECT_JSON}', encoding='utf-8'))${1})"
}

FIRMWARE_REPO="$(read_json "['firmware']['repository']")"
FIRMWARE_COMMIT="$(read_json "['firmware']['commit']")"
ENVIRONMENT="$(read_json "['environment']")"
ARTIFACT_FOLDER="$(read_json "['release']['artifactFolder']")"
STAMP="$(date +%Y%m%d-%H%M%S)"
EXPORT_DIR="${EXPORT_ROOT}/${STAMP}-${ENVIRONMENT}"
SOURCE_DIR="${BUILD_ROOT}/firmware"

export PATH="${HOME}/.local/bin:${PATH}"
export PIP_BREAK_SYSTEM_PACKAGES=1

if ! python3 -m platformio --version >/dev/null 2>&1; then
    python3 -m pip install --user --break-system-packages platformio
fi

rm -rf "${BUILD_ROOT}"
mkdir -p "${BUILD_ROOT}" "${EXPORT_DIR}"
git init -q "${SOURCE_DIR}"
git -C "${SOURCE_DIR}" remote add origin "${FIRMWARE_REPO}"
git -C "${SOURCE_DIR}" fetch -q --depth 1 origin "${FIRMWARE_COMMIT}"
git -C "${SOURCE_DIR}" checkout -q --detach FETCH_HEAD
test "$(git -C "${SOURCE_DIR}" rev-parse HEAD)" = "${FIRMWARE_COMMIT}"
git -C "${SOURCE_DIR}" apply --check "${ROOT}/source/patches/zdeck-full-source.patch"
git -C "${SOURCE_DIR}" apply "${ROOT}/source/patches/zdeck-full-source.patch"

TEST_OUT="${BUILD_ROOT}/policy-tests"
mkdir -p "${TEST_OUT}"
for name in display_policy gps_quality_policy map_state mesh_mode_policy update_policy; do
    case "${name}" in
        display_policy) source_name="ZDeckDisplayPolicy.cpp" ;;
        gps_quality_policy) source_name="ZDeckGpsQualityPolicy.cpp" ;;
        map_state) source_name="ZDeckMapState.cpp" ;;
        mesh_mode_policy) source_name="ZDeckMeshModePolicy.cpp" ;;
        update_policy) source_name="ZDeckUpdatePolicy.cpp" ;;
    esac
    g++ -std=c++17 -Wall -Wextra -Werror -I"${SOURCE_DIR}/src" \
        "${SOURCE_DIR}/src/itsz/${source_name}" "${SOURCE_DIR}/tests/itsz/test_zdeck_${name}.cpp" \
        -o "${TEST_OUT}/${name}"
    "${TEST_OUT}/${name}"
done

cd "${SOURCE_DIR}"
python3 -m platformio run -e "${ENVIRONMENT}"
python3 -m platformio run -e "${ENVIRONMENT}" -t buildfs
python3 -m platformio run -e "${ENVIRONMENT}" -t mtjson
python3 "${ROOT}/tools/finalize-firmware-metadata.py" ".pio/build/${ENVIRONMENT}"

find ".pio/build/${ENVIRONMENT}" -maxdepth 1 -type f \
    \( -name '*.bin' -o -name '*.elf' -o -name '*.map' -o -name '*.json' \) \
    -print -exec cp -v '{}' "${EXPORT_DIR}/" \;
printf '%s\n' "${FIRMWARE_COMMIT}" > "${EXPORT_DIR}/source-head.txt"
printf '%s\n' "${ARTIFACT_FOLDER}" > "${EXPORT_DIR}/artifact-folder.txt"
git status --short > "${EXPORT_DIR}/source-status.txt"
printf 'Build complete: %s\n' "${EXPORT_DIR}"
