class TrieNode:

    def __init__(self, value):
        self.data = value
        self.children = [None] * 26
        self.is_end_chr = False
