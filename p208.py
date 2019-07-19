class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        node = self.head
        for c in list(word):
            if c in node:
                node = node[c]
            else:
                node[c] = dict()
                node = node[c]
        node['word_mark'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.head

        for c in list(word):
            if c in node:
                node = node[c]
            else:
                return False

        return 'word_mark' in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.head

        for c in list(prefix):
            if c in node:
                node = node[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)