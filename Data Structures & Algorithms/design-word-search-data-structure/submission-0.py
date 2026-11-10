class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):                     # Search from the given index and Trie node.

            for i in range(index, len(word)):     # Process remaining characters.
                char = word[i]

                if char == ".":                   # A dot can match any single character.
                    for child in node.children.values():
                        if dfs(i + 1, child):      # Search remaining characters from this child.
                            return True           # One matching path is sufficient.

                    return False                  # None of the child paths matched.

                if char not in node.children:     # Normal character is missing.
                    return False

                node = node.children[char]        # Move to the matching child node.

            return node.is_end                    # Check whether a complete word was found.

        return dfs(0, self.root)                   # Start searching from index 0 and the root.


