import Levenshtein
from trie_node import TrieNode



class PrefixTree:

    def __init__(self):

        self.root = TrieNode('')

    def insert(self, filename, original_sentence, sentence, row_num):

        words = sentence.split()
        current = self.root

        for i in range(len(words)):
            word = words[i]


            current = current.children.setdefault(word, TrieNode(' '.join(words[:i + 1])))

            current.word = sentence
            current.original_sentence = original_sentence

            if i == len(words) - 1:
                current.is_end = True

            current.offset.setdefault(filename, []).append(row_num)

    def find_sentences_containing(self, user_input):

        word_list = user_input.split()
        score = len(user_input) * 2
        matched_sentences = []

        self.find_exact_match(self.root,word_list,0,[],matched_sentences,score)


        self.find_with_levenshtein(self.root, word_list, matched_sentences, score)
        return matched_sentences



    def find_with_levenshtein(self, root, word_list, matched_sentences, score):
        total_changes = 0
        modified_input = ""
        self.dfs_find_with_total_levenshtein(root, word_list, 0, [], matched_sentences, score, total_changes,
                                             modified_input)





    def find_exact_match(self, current, word_list, index, path, matched_sentences, score):

        if index == len(word_list):
            self.collect_words_with_offsets(current, ' '.join(path), matched_sentences, score)
            return

        word = word_list[index]
        for child_word, child_node in current.children.items():
            if word ==  child_word:
                new_path = path + [child_word]

                self.find_exact_match(child_node, word_list, index + 1, new_path,
                                                     matched_sentences, score)

        for child_word, child_node in current.children.items():
            self.find_exact_match(child_node, word_list, index, path, matched_sentences, score)





    def dfs_find_with_total_levenshtein(self, current, word_list, index, path, matched_sentences, score, total_changes,
                                        modified_input):

        if index == len(word_list):
            if total_changes <= 1:
                word_list_str = ' '.join(word_list)

                found, index = self.find_deleted_letter_index(word_list_str, modified_input)
                if found:
                    score += self.add_sub_calculate_score(index)
                found, index = self.find_added_letter_index(word_list_str, modified_input)
                if found:
                    score += self.add_sub_calculate_score(index)
                found, index = self.find_different_indices(word_list_str, modified_input)
                if found:
                    score += self.change_char_calculate_score(index)


                self.collect_words_with_offsets(current, ' '.join(path), matched_sentences, score)

            return

        word = word_list[index]  # The current word in the user's input

        # Explore all child nodes to find possible matches with Levenshtein distance
        for child_word, child_node in current.children.items():
            levenshtein_distance = Levenshtein.distance(word, child_word)

            # Only continue if total changes remain <= 1
            if total_changes + levenshtein_distance <= 1:
                new_total_changes = total_changes + levenshtein_distance
                new_path = path + [child_word]

                # Append the altered word to modified_input
                new_modified_input = modified_input + (child_word if levenshtein_distance > 0 else word)

                # Recur for the next word and deeper levels of the Trie
                self.dfs_find_with_total_levenshtein(child_node, word_list, index + 1, new_path,
                                                     matched_sentences, score, new_total_changes, new_modified_input)

        # If no match is found at this level, recursively search the children of the current node for the same word
        for child_word, child_node in current.children.items():
            # Recur to search the same word in deeper children nodes
            self.dfs_find_with_total_levenshtein(child_node, word_list, index, path, matched_sentences, score,
                                                 total_changes, modified_input)

    def collect_words_with_offsets(self, node, current_sentence, collected_sentences, score):

        if node.is_end:
            # Add the original sentence and its offset to the collected sentences
            collected_sentences.append((node.original_sentence, node.offset, score))

        # Recur through the children of the current node
        for word, child_node in node.children.items():
            self.collect_words_with_offsets(child_node, f"{current_sentence} {word}".strip(), collected_sentences,
                                            score)

    def find_different_indices(self, user_input, modified_input):

        if len(user_input) == len(modified_input):
            for i in range(len(user_input)):
                if user_input[i] != modified_input[i]:
                    return True, i
        return False, -1

    def find_added_letter_index(self, user_input, modified_input):
        if len(user_input) >= len(modified_input):
            return False, -1


        if len(user_input) - 1 == len(modified_input):  # Ensure user_input is longer by 1 letter

            for i in range(0, len(user_input)):

                original_word = user_input[:i + 1]
                modified_word = modified_input[:i + 1]
                if original_word == modified_word:
                    continue  # Skip if original word is longer, no letter added
                else:
                    return True, i
            return True, len(modified_input) - 1
        return False, -1

    # num one
    def find_deleted_letter_index(self, user_input, modified_input):
        if len(user_input) <= len(modified_input):
            return False, -1


        if len(user_input) - 1 == len(modified_input):  # Ensure user_input is longer by 1 letter

            for i in range(0, len(modified_input)):

                original_word = user_input[:i + 1]
                modified_word = modified_input[:i + 1]
                if original_word == modified_word:
                    continue  # Skip if original word is longer, no letter added
                else:
                    return True, i
            return True, len(user_input) - 1
        return False, -1

    def add_sub_calculate_score(self, index):
        index = 4 if index >= 3 else index
        return -1 * (10 - index * 2)

    def change_char_calculate_score(self, index):
        index = 4 if index >= 4 else index
        return -1 * (5 - index)