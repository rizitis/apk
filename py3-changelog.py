import os
from distutils.version import LooseVersion

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

    print("Old packages:")
    print(old_packages)  # print old package list

    print("New packages:")
    print(new_packages)  # print new package list

    # Loop through each new package to classify it
    for new_package in new_packages:
        # Skip lines with timestamps or any other unwanted entries
        if new_package.startswith("#"):
            continue

        print(f"Processing package: {new_package}")
        parts = new_package.split('-')
        print(f"Parts: {parts}")  # Check how the package is being split

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
                old_version_num = old_version[1]  # Assuming version is at index 1
                new_version_num = new_version[1]  # Assuming version is at index 1

                # Compare using LooseVersion to handle version numbers properly
                if LooseVersion(old_version_num) != LooseVersion(new_version_num):
                    print(f"Version change detected for {new_package}: {old_version_num} -> {new_version_num}")
                    changelog_entries.append(f"Upgraded>{new_package} :")

            if len(old_version) >= 3 and len(new_version) >= 3:
                old_release_num = old_version[2]  # Assuming release is at index 2
                new_release_num = new_version[2]  # Assuming release is at index 2

                if old_release_num != new_release_num:
                    print(f"Release change detected for {new_package}: {old_release_num} -> {new_release_num}")
                    changelog_entries.append(f"Rebuilt>{new_package} :")

    # Check for removed packages (those in the old file but not in the new file)
    for old_package in old_packages:
        if old_package not in new_set:
            changelog_entries.append(f"Removed>{old_package} :")

    # Print the changelog entries to be written
    print("Changelog entries to be written:")
    print("\n".join(changelog_entries))

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
