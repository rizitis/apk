#!/bin/bash
# shellcheck disable=SC2227,SC2188

CWD=$(pwd)
echo "$CWD"
FILENAME="BIN_NAME"

OUTPUT_FILE="$CWD"/apk.list.TXT
UPDATE=$(date)
echo "# $UPDATE" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

find ./ -type f -name "$FILENAME" -exec cat {} >> "$OUTPUT_FILE" \;

echo "Done."
