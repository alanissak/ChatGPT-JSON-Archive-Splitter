import json
import re
import os
import time

def sanitize_filename(name):
    """Sanitize the name to make it a valid filename, removing characters unsuitable for file names."""
    return re.sub(r'[\/:*?"<>|]', '', name)

def extract_conversation_id(entry):
    """Extract the 'conversation_id' from the entry."""
    return entry.get("conversation_id", "Untitled")

def parse_and_save_entries_from_file(file_path):
    output_dir = 'Outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist

    with open(file_path, 'r') as file:
        json_line = file.read()

    entries = []
    start_idx = 0
    process_counter = 0
    while True:
        if process_counter % 10 == 0:  # Slow down every 10 entries
            time.sleep(1)  # Sleep for 1 second to reduce load
        start = json_line.find('{"title":', start_idx)
        if start == -1:
            break
        end = json_line.find('"}, {"title":', start)
        if end == -1:
            entry_json = json_line[start:] + '}'  # Handle the last entry
        else:
            entry_json = json_line[start:end+2]  # Include `"},` to complete the entry

        try:
            entry = json.loads(entry_json)
            entries.append(entry)
            # Extract the conversation ID for the filename
            conversation_id = extract_conversation_id(entry)
            sanitized_id = sanitize_filename(conversation_id)
            filename = os.path.join(output_dir, f"{sanitized_id}.json")
            with open(filename, 'w') as file:
                json.dump(entry, file, indent=4)
            print(f"Saved: {filename}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON at positions {start} to {end if end != -1 else 'end of file'}: {e}")
            print(f"Problematic JSON: {entry_json}")
        start_idx = end + 3 if end != -1 else len(json_line)
        process_counter += 1

# Specify the path to your JSON file
json_file_path = 'conversations.json'
parse_and_save_entries_from_file(json_file_path)
