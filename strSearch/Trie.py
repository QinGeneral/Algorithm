from TrieNode import TrieNode


class Trie:

    def __init__(self):
        self.head: TrieNode = TrieNode("/")
        self.start_i = ord('a')

    def insert(self, s):
        if type(s) != str or len(s) == 0:
            return
        temp = self.head
        for ch in s:
            index = ord(ch) - self.start_i
            if index < 0 or index > 25:
                continue
            if temp.children[index] is None:
                temp.children[index] = TrieNode(ch)
            temp = temp.children[index]
        temp.is_end_chr = True

    def find(self, s):
        if type(s) != str or len(s) == 0:
            return False
        temp = self.head
        for ch in s:
            index = ord(ch) - self.start_i
            if index < 0 or index > 25:
                continue
            if temp.children[index] is None:
                return False
            temp = temp.children[index]

        if temp.is_end_chr is False:
            return False
        return True

    def print(self, node):
        is_all_none = True
        for i in node.children:
            if i is not None:
                print(i.data)
                self.print(i)



trie = Trie()
trie.insert('abc')
trie.insert('abd')
trie.insert('cba')
print(trie.find('ab'))
print(trie.find('abc'))
print(trie.find('abcd'))
print(trie.find('cba'))
trie.print(trie.head)
