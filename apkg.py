import json
import tkinter as tk
import requests

# Function to load and parse the JSON from URL
def load_json():
    url = "https://raw.githubusercontent.com/rizitis/apk/refs/heads/main/repo_contents.json"
    response = requests.get(url)
    return response.json()

# Function to update the listbox based on search query
def update_listbox(search_query, listbox, tar_lz4_names, start_index, end_index):
    listbox.delete(0, tk.END)  # Clear the listbox
    for name in tar_lz4_names[start_index:end_index]:
        if search_query.lower() in name.lower():
            listbox.insert(tk.END, name)

# Function to create the GUI with pagination
def create_gui():
    # Load data and filter .tar.lz4 names
    files_data = load_json()
    tar_lz4_names = [item['name'].replace('.tar.lz4', '') for item in files_data if item['name'].endswith('.tar.lz4')]

    items_per_page = 50
    page_number = 0

    # Function to display the current page
    def display_page():
        start_index = page_number * items_per_page
        end_index = start_index + items_per_page
        update_listbox(search_entry.get(), listbox, tar_lz4_names, start_index, end_index)

    # Function for next page
    def next_page():
        nonlocal page_number
        if (page_number + 1) * items_per_page < len(tar_lz4_names):
            page_number += 1
            display_page()

    # Function for previous page
    def prev_page():
        nonlocal page_number
        if page_number > 0:
            page_number -= 1
            display_page()

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

    # Add buttons for pagination
    prev_button = tk.Button(root, text="Previous", command=prev_page, font=("Arial", 12))
    prev_button.pack(side=tk.LEFT, padx=5, pady=5)

    next_button = tk.Button(root, text="Next", command=next_page, font=("Arial", 12))
    next_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Add search event handler to filter the list
    def on_search_change(*args):
        display_page()

    search_entry.bind("<KeyRelease>", on_search_change)

    # Display the initial page
    display_page()

    # Run the application
    root.mainloop()

# Run the GUI
create_gui()
