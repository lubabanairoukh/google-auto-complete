import auto_complete_data as acd
import string

# Define constant for offset value in the file
OFFSET_VALUE = 0

def clean_sentence(sentence):
    """
    Cleans the input sentence by stripping extra whitespace between words.

    Args:
        sentence (str): The input sentence to be cleaned.

    Returns:
        str: The cleaned sentence with extra spaces removed.
    """
    cleaned_sentence = ' '.join(sentence.split())  # Normalize spaces between words
    return cleaned_sentence

def lowercase_and_remove_punctuation(sentence):
    """
    Converts the sentence to lowercase and removes punctuation.

    Args:
        sentence (str): The input sentence to be processed.

    Returns:
        str: The sentence in lowercase and without punctuation.
    """
    lowercase_sentence = sentence.lower()  # Convert sentence to lowercase
    translator = str.maketrans('', '', string.punctuation)  # Create a translation table to remove punctuation
    cleaned_sentence = lowercase_sentence.translate(translator)  # Remove punctuation using translate()
    return cleaned_sentence

def get_nodes(tree, sentence):
    """
    Preprocesses the sentence and finds matching nodes in the Trie.

    Args:
        tree (PrefixTree): The prefix tree containing the stored sentences.
        sentence (str): The user input sentence.

    Returns:
        list: A list of Trie nodes that match the cleaned and processed sentence.
    """
    sentence = clean_sentence(sentence)  # Clean the sentence by normalizing spaces
    sentence = lowercase_and_remove_punctuation(sentence)  # Lowercase and remove punctuation
    nodes_trie = tree.find_sentences_containing(sentence)  # Find matching nodes in the Trie
    return nodes_trie

def display_matches(tree, sentence):
    """
    Displays matching results from the Trie for the given sentence.

    Args:
        tree (PrefixTree): The prefix tree containing the stored sentences.
        sentence (str): The user input sentence.

    Returns:
        None: Prints the matching results or a message if no matches are found.
    """
    nodes_trie = get_nodes(tree, sentence)  # Get the nodes that match the cleaned sentence
    # sort -> score
    sorted_nodes = sorted(nodes_trie, key=lambda node: node[2], reverse=True)
    top_5_nodes = sorted_nodes[:5]  # Create a shallow copy of the nodes list
    # nodes_trie = nodes_trie[:]  # Create a shallow copy of the nodes list

    if not nodes_trie:
        # If no matches found, print a message
        print("nothing to show")
        return

    print("Here are 5 suggestions:")
    suggestions_index = 1

    # Print the matched sentences, their offsets, and scores
    for sentence, offsets_dict, score in top_5_nodes:
        # Extract the first filename and offset from the offsets dictionary
        filename, offset_list = next(iter(offsets_dict.items()))
        offset_value = offset_list[OFFSET_VALUE]

        # Create an AutoCompleteData object to store the match information
        result = acd.AutoCompleteData(
            sentence.strip(),  # Strip whitespace from the original sentence
            filename,          # Filename where the sentence was found
            offset_value,      # Line number or offset in the file
            score              # The match score
        )
        # print(result)  # Print the result
        print(f"{suggestions_index}. {result.completed_sentence}({result.source_text} {result.offset})")
        suggestions_index += 1



