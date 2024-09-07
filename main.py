import os

import search_system as search_sy
import main as pt
from prefix_tree import PrefixTree

root_directory = r'C:\Users\97254\Desktop\excellenteam\Google_Project\pandas'
type_of_file = ".txt"

ZIP_PATH = r'C:\Users\lubab\Downloads\Archive.zip'
EXTRACT_DIR = r'C:\Users\lubab\Documents\Archive'  # Define your permanent extraction directory

# Define logging
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
logs_dir = os.path.join(CURR_DIR, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)


def build_tree():
    """
    Builds a prefix tree (Trie) from text files located in the specified root directory.

    This function walks through the `root_directory` and processes all files ending with
    the specified file type (`type_of_file`). It reads each file line by line, processes
    each sentence by cleaning and removing punctuation, and inserts the sentences into
    a Trie structure, associating them with the line number in which they appear.

    Returns:
        tree (PrefixTree): A populated prefix tree containing the sentences from the files.
    """
    tree = pt.PrefixTree()  # Initialize the prefix tree (Trie)

    # Traverse the root directory and its subdirectories for the text files
    for subdir, dirs, files in os.walk(root_directory):
        for file_text in files:
            if file_text.endswith(type_of_file):
                # Construct the full file path and print a message for progress
                file_path = os.path.join(subdir, file_text)
                print(f"Processing file: {file_path}")

                # Read each file line by line
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, start=1):  # Enumerate lines starting from 1
                        original_sentence = line.strip()  # Clean up whitespace around the line

                        # Clean and normalize the sentence by removing punctuation and lowering case
                        cleaned_sentence = search_sy.lowercase_and_remove_punctuation(
                            search_sy.clean_sentence(original_sentence)
                        )

                        # Insert the cleaned sentence into the Trie with the line number (row_num)
                        tree.insert(file_text, original_sentence, cleaned_sentence, line_number)

    print("Processed sentences from the files.")
    return tree  # Return the populated Trie


def main():
    """
    Main function to build the prefix tree and perform searches.

    This function first builds the prefix tree by calling `build_tree()`. Once the tree
    is built, it takes user input (a search sentence) and displays matching results
    using the `display_matches()` function from the search system.
    """
    print("Building prefix tree from scratch...")

    # Build the prefix tree from the files in the root directory
    tree = build_tree()

    cumulative_user_input = ""

    while True:
        user_input = input("Enter your text: ")

        if user_input == '#':
            # Reset the cumulative input
            cumulative_user_input = ""
            print("Input has been reset. Start a new search.")
        else:
            # Add the new input to the cumulative input
            cumulative_user_input +=user_input if cumulative_user_input else user_input

            # Display matching results based on the cumulative input
            search_sy.display_matches(tree, cumulative_user_input)
            print(cumulative_user_input)


if __name__ == "__main__":
    """
    Entry point of the script.

    This block ensures that the `main()` function runs when the script is executed directly.
    """
    main()
