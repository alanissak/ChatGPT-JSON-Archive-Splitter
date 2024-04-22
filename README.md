# ChatGPT-JSON-Archive-Splitter

This Python script will take in your single, large, one-line JSON ChatGPT conversation archive file and split each conversation into its own JSON file. Each split JSON file will be sent to the `/outputs` folder and named after the chat's `conversation_id` variable.

## How it works

The script parses the single-line JSON archive file which contains all your chats you have had with ChatGPT. You can request this archive file through your ChatGPT user settings panel. As it parses, it will save each of the detected chat entries into its own file. This is useful if you plan on creating a more advanced chat search tool or simply a way to "offload" your chats off ChatGPT and keep a nice archive of all your previous conversations.

Here is a brief rundown of the entire process:

1. **Analyzing The Archive:** The script looks through the entire JSON archive file and reads it into memory.
2. **Identifying Entries:** The script then looks through the JSON file to identify the start and finish of each entry utilizing specific specified strings. Note: I am currently a newbie when it comes to understanding how JSON files work. I feel that there is a simpler way but with my current knowledge, this is what I was able to think of as my "simplest" method.
3. **Parsing:** The Python string is then parsed using Python's `json.loads()` function. The function converts the JSON strings into a Python dictionary.
4. **Saving:** Each conversation is then saved into its own JSON file. The filename is derived from the `conversation_id` variable located within each chat entry.

### Directory Structure

- `Outputs/`: This is the directory where all converter JSON files are saved. These are where your individual chats are stored after being processed.

## Prerequisites

Python libraries: `json`, `re`, `os`, and `time`.

## Usage

You only need two things:

1. Your `conversations.json` file that will be sent to your email from ChatGPT after requesting for it.
2. The `jsonSplitter.py` script.

1. Place your `conversations.json` file in the same directory as the `jsonSplitter.py` script. You can also modify the `json_file_path` variable if you want to keep the `conversations.json` file in another directory (does it really matter?).
2. Run the `jsonSplitter.py` script.
3. Watch the magic happen.

### Limitations

This script was designed to take in the `conversations.json` archive as is. ChatGPT gives you this file with all of the JSON contents written into a single line so be sure to know that formatting it could break the script. I personally have not tested this script out with a formatted `conversations.json` file as it's an extra unnecessary step, however, you can give it a shot if you'd like to test the capabilities of the Python script.

### Function Descriptions

1. sanitize_filename(name): Removes characters from the conversation_id that are unsuitable for file names.
2. extract_conversation_id(entry): Extracts the conversation_id from a conversation entry.
3. parse_and_save_entries_from_file(file_path): Main function that processes the JSON file and saves each entry as a separate file.
