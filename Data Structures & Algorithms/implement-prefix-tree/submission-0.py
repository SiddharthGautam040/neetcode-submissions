class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        i = 0
        while i < len(word):
            c = ord(word[i]) - ord('a')
            
            if not node.children[c]:
                node.children[c] = Node()
            
            node = node.children[c]
            i += 1
        
        node.endWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for ele in word:
            i = ord(ele) - ord('a')
            if not node.children[i]:
                return False
        
            node = node.children[i]
        return node.endWord
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ele in prefix:
            i = ord(ele) - ord('a')
            if not node.children[i]:
                return False
        
            node = node.children[i]
        return True
        
class Node:

    def __init__(self):
        self.children = [False] * 26
        self.endWord = False