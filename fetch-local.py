import os
import json

# Get the current working directory
repo_path = os.getcwd()

# Function to generate the JSON file in the desired format
def generate_json():
    file_info = []

    # Traverse the repo directory
    for root, dirs, files in os.walk(repo_path):
        # Skip the .git directory and its contents
        if '.git' in root:
            continue

        for file in files:
            # Add file information to the list in the desired format
            file_info.append({
                'name': file,
                'path': os.path.join("https://raw.githubusercontent.com/rizitis/apk/refs/heads/main", file),
                'type': 'file'
            })

    # Save the output to a JSON file
    with open("apk_repo_contents.json", "w") as json_file:
        json.dump(file_info, json_file, indent=4)

# Call the function to generate the JSON
generate_json()
