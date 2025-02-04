#!/bin/bash
# shellcheck disable=SC2227,SC2188

CWD=$(pwd)
echo "$CWD"


OUTPUT_FILE="$CWD"/apk.list.TXT



make_update() {
mv "$OUTPUT_FILE" /tmp
UPDATE=$(date)
echo "# $UPDATE" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

for tar_file in "$CWD"/*.tar.lz4; do
    # Check if the file exists (in case there are no matches)
    if [ -e "$tar_file" ]; then
        # Extract the package name by removing the ".tar.lz4" extension
        PKG=$(basename "$tar_file" .tar.lz4)
        # Attempt to extract $PKG/BIN_NAME and append it to $OUTPUT_FILE
        tar --use-compress-program=lz4 -xOf "$tar_file" "$PKG/BIN_NAME" >> "$OUTPUT_FILE" 2>> "$OUTPUT_FILE"

        # Check for errors during extraction
        if [ $? -ne 0 ]; then
            echo "Warning: Failed to extract '$PKG/BIN_NAME' from $tar_file" >> "$OUTPUT_FILE"
        fi
    else
        echo "No .tar.lz4 files found in $CWD."
        break
    fi
done

echo "apk.list.TXT Done."
}




create_json() {
echo "Creating json file..."
python fetch-local.py
wait
sed -i 's|/home/omen/GITHUB|https://github.com/rizitis|g' ./repo_contents.json
echo "create json Done"
}

create_changelog() {
echo "Creating ChangeLog.txt"
python py3-changelog.py
}


finally_push() {
git pull
git add .
git commit -s -m "update"
git push
echo "finally git push Done"
}


make_update
create_json
create_changelog
finally_push
