
# Google Autocomplete Project

## Overview

The Google Autocomplete Project is a Python-based search system that mimics the functionality of Google's autocomplete feature. The project uses the **Levenshtein Distance Algorithm** to provide suggestions for user inputs based on a pre-defined dataset of search terms. The system efficiently predicts and completes user queries as they type, offering a fast and accurate user experience.

## Features

- **Trie Data Structure**: Utilizes a Trie for efficient insertion and search operations to handle autocomplete suggestions.
- **Levenshtein Distance**: Implements the Levenshtein Distance Algorithm to provide intelligent and context-aware suggestions, even when user input contains typos or misspellings.
- **Auto-update Trie**: Continuously updates the Trie with new search queries, adapting to changing user behavior.
- **Efficient Search**: Provides fast query suggestions by optimizing both the search and autocomplete operations.

## Technologies Used

- **Programming Language**: Python
- **Algorithm**: Levenshtein Distance for fuzzy matching
- **Data Structure**: Trie (Prefix Tree)
  
## How it Works

1. **Input Processing**: The system accepts user input in real-time as a query string.
2. **Search Matching**: It uses the Trie data structure to look up words that match the prefix of the input string.
3. **Fuzzy Matching**: For incomplete or incorrect entries, the Levenshtein algorithm is applied to calculate the edit distance between the user input and existing terms, providing relevant suggestions.
4. **Real-Time Updates**: New search terms are dynamically added to the Trie and the search space is continuously updated.



