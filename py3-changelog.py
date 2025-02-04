import os

def compare_version_parts(old_version, new_version):
    # Compare each part (major, minor, patch) one by one
    old_parts = old_version.split('.')
    new_parts = new_version.split('.')

    # Normalize the length of parts, adding zeroes for missing parts
    max_len = max(len(old_parts), len(new_parts))
    old_parts.extend(['0'] * (max_len - len(old_parts)))
    new_parts.extend(['0'] * (max_len - len(new_parts)))

    for old_part, new_part in zip(old_parts, new_parts):
        # Compare parts as integers to handle version numbers correctly
        if int(old_part) < int(new_part):
            return True  # old version is less than new version
        elif int(old_part) > int(new_part):
            return False  # old version is greater than new version

    return False  # Versions are equal

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
        # Skip lines with timestamps or any other unwanted entries
        if new_package.startswith("#"):
            continue

        parts = new_package.split('-')

        if new_package not in old_set:
            # If the package is in the new file but not in the old file, it was added
            changelog_entries.append(f"Added>{new_package} :")
        else:
            # If the package exists in both files, check version
            old_version = [pkg for pkg in old_packages if pkg.split('-')[0] == new_package.split('-')[0]]
            new_version = new_package.split('-')
            old_version = old_version[0].split('-') if old_version else []

            # Ensure there are at least 2 parts (package name and version) for comparison
            if len(old_version) >= 2 and len(new_version) >= 2:
                old_version_num = old_version[1]  # Extract version
                new_version_num = new_version[1]  # Extract version

                # Compare the versions using the helper function
                if compare_version_parts(old_version_num, new_version_num):
                    changelog_entries.append(f"Upgraded>{new_package} :")

            if len(old_version) >= 3 and len(new_version) >= 3:
                old_release_num = old_version[2]  # Extract release number
                new_release_num = new_version[2]  # Extract release number

                if old_release_num != new_release_num:
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
