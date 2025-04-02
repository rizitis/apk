#!/bin/bash
# shellcheck disable=SC2227,SC2188

CWD=$(pwd)
echo "$CWD"


OUTPUT_FILE="$CWD"/apk.list.TXT
DATE=$(date)


make_update() {
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

finally_push() {
    git pull

    # Add changes to staging
    git add .

    # Ask the user for a custom commit message
    read -p "Enter commit message: " commit_message

    # Commit with the user's message
    git commit -s -m "$commit_message"

    # Push the changes
    git push

    echo "finally git push Done"
}


create_changelog() {
    # Set the output changelog file path
    CHANGELOG_FILE="$CWD"/CHANGELOG.md

    # Write the Changelog header and commit history to the file
    echo "# Changelog" > "$CHANGELOG_FILE"
    echo "Generated on: $(date)" >> "$CHANGELOG_FILE"
    echo "" >> "$CHANGELOG_FILE"

    # Retrieve the Git log with commit date and other details, including unpushed commits
    git log --pretty=format:"* %h - %s (%an) [%ad]" --date=short >> "$CHANGELOG_FILE"

    echo "" >> "$CHANGELOG_FILE"
    echo "## Tags" >> "$CHANGELOG_FILE"
    git tag --list | while read -r tag; do
        echo "* Tag: $tag" >> "$CHANGELOG_FILE"
    done

    # Display the changelog in the terminal (optional)
    cat "$CHANGELOG_FILE"

    # Print confirmation message
    echo "Changelog created at $CHANGELOG_FILE"
}

first_push() {
    # Pull latest changes first to get any new changes from the remote
    git pull

    # Add all changes to staging
    git add .

    # Ask the user for a commit message
    read -p "Enter commit message: " commit_message

    echo "$DATE: $commit_message" > "LAST_MESSG.nfo"
    # Commit with the user's message
    git commit -s -m "$commit_message"

    # Push the changes to the remote repository
    git push
}

finally_push(){
    git add .
    git commit -s -m "$commit_message"
    # Print success message
    echo "finally git push Done"
    git push
}

make_update
create_json
create_changelog
first_push
finally_push
