class TrieNode:
    """
    Represents a single node in the Trie (prefix tree) structure.

    Each node holds a portion of a sentence and links to child nodes that continue
    building words or phrases from the stored text.

    Attributes:
        text (str): The text or word that this node represents.
        children (dict): A dictionary where keys are the next words and values are TrieNode objects.
        is_end (bool): Marks if this node represents the end of a complete sentence or phrase.
        offset (dict): Stores the file names and corresponding line numbers (or positions) where the sentence appears.
        original_sentence (str): The original, unprocessed sentence as it was added to the Trie.
    """
    def __init__(self, text=''):
        """
        Initializes a TrieNode with optional text.

        Args:
            text (str, optional): The text or word this node represents. Default is an empty string.
        """
        self.text = text  # Store the current word or partial sentence at this node
        self.children = dict()  # Initialize an empty dictionary for child nodes
        self.is_end = False  # Flag to indicate if this node marks the end of a sentence
        self.offset = {}  # Dictionary to store file names and corresponding line numbers
        self.original_sentence = None  # Stores the complete, original sentence for reference
