import json
import tkinter as tk
import requests

# Function to load and parse the JSON from URL
def load_json():
    url = "https://raw.githubusercontent.com/rizitis/apk/refs/heads/main/apk_repo_contents.json"
    response = requests.get(url)
    files_data = response.json()

    # Extract names of the .tar.lz4 files
    tar_lz4_names = [item['name'].replace('.tar.lz4', '') for item in files_data if item['name'].endswith('.tar.lz4')]
    return tar_lz4_names

# Function to update listbox based on search query
def update_listbox(search_query, listbox, tar_lz4_names):
    listbox.delete(0, tk.END)  # Clear the listbox
    for name in tar_lz4_names:
        if search_query.lower() in name.lower():
            listbox.insert(tk.END, name)

# Function to create the GUI
def create_gui():
    # Load the data
    tar_lz4_names = load_json()

    # Create the main window
    root = tk.Tk()
    root.title("APK Slackware Repo")

    # Create a label to display the names
    label = tk.Label(root, text="List of package file names:", font=("Arial", 14))
    label.pack(pady=10)

    # Create a search entry
    search_label = tk.Label(root, text="Search:", font=("Arial", 12))
    search_label.pack(pady=5)

    search_entry = tk.Entry(root, font=("Arial", 12))
    search_entry.pack(pady=5)

    # Create a listbox to show the file names
    listbox = tk.Listbox(root, height=15, width=50, font=("Arial", 12))
    listbox.pack(pady=10)

    # Insert the extracted names into the listbox
    for name in tar_lz4_names:
        listbox.insert(tk.END, name)

    # Add a search event handler to update listbox based on the search
    def on_search_change(*args):
        search_query = search_entry.get()
        update_listbox(search_query, listbox, tar_lz4_names)

    search_entry.bind("<KeyRelease>", on_search_change)

    # Run the application
    root.mainloop()

# Run the GUI
create_gui()
