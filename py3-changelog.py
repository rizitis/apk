import os

def compare_package_versions(old_file, new_file, changelog_file='ChangeLog.txt'):
    # Read in the old and new files
    with open(old_file, 'r') as f:
        old_packages = f.read().splitlines()

    with open(new_file, 'r') as f:
        new_packages = f.read().splitlines()

    # Create a set for fast lookup
    old_set = set(old_packages)
    new_set = set(new_packages)

    # Prepare the output for the changelog
    changelog_entries = []

    # Loop through each new package to classify it
    for new_package in new_packages:
        # Skip lines with timestamps
        if new_package.startswith("#"):
            continue

        if new_package not in old_set:
            # If the package is in the new file but not in the old file, it was added
            changelog_entries.append(f"Added>{new_package} :")
        else:
            # If the package exists in both files, check version
            old_version = [pkg for pkg in old_packages if pkg.split('-')[0] == new_package.split('-')[0]]
            new_version = new_package.split('-')
            old_version = old_version[0].split('-') if old_version else []
            if old_version and new_version and old_version[1] != new_version[1]:
                # If the version numbers are different, it has been upgraded
                changelog_entries.append(f"Upgraded>{new_package} :")
            elif old_version and new_version and old_version[2] != new_version[2]:
                # If the release numbers are different, it has been rebuilt
                changelog_entries.append(f"Rebuilt>{new_package} :")

    # Check for removed packages (those in the old file but not in the new file)
    for old_package in old_packages:
        if old_package not in new_set:
            changelog_entries.append(f"Removed>{old_package} :")

    # Prepare to write to ChangeLog.txt
    if os.path.exists(changelog_file):
        # If the changelog file exists, prepend the new entries
        with open(changelog_file, 'r') as f:
            existing_content = f.read()

        # Write the new entries on top of the existing content with a separator
        with open(changelog_file, 'w') as f:
            f.write("==== New Changes ====\n")  # Separator
            f.write("\n".join(changelog_entries) + "\n")
            f.write("\n" + existing_content)
    else:
        # If the file does not exist, create it and write the entries
        with open(changelog_file, 'w') as f:
            f.write("==== New Changes ====\n")  # Separator
            f.write("\n".join(changelog_entries) + "\n")

# Call the function with your file names
old_file = '/tmp/apk.list.TXT'
new_file = 'apk.list.TXT'
compare_package_versions(old_file, new_file)
