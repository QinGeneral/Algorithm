class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEndOfWord = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word is None or len(word) == 0:
            return
        trie = self
        for ch in word:
            index = ord(ch) - ord("a")
            if trie.children[index] is None:
                trie.children[index] = Trie()
            trie = trie.children[index]
        trie.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word is None or len(word) == 0:
            return False
        trie = self
        for ch in word:
            index = ord(ch) - ord("a")
            if trie.children[index] is None:
                return False
            trie = trie.children[index]
        return trie.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix is None or len(prefix) == 0:
            return False
        trie = self
        for ch in prefix:
            index = ord(ch) - ord("a")
            if trie.children[index] is None:
                return False
            trie = trie.children[index]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # 返回 True
print(trie.search("app"))  # 返回 False
print(trie.startsWith("app"))  # 返回 True
trie.insert("app")
print(trie.search("app"))  # 返回 True
