class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root

        i = 0
        while i < len(word):
            c = ord(word[i]) - ord('a')
            
            if not node.children[c]:
                node.children[c] = Node()
            
            node = node.children[c]
            i += 1
        
        node.endWord = True

    def search(self, word: str, curr_node = False) -> bool:
        node = curr_node or self.root 
        i = 0
        while i < len(word):
            ele = word[i]
            if ele == ".":
                for child in node.children:
                    if child and self.search(word[i+1:], child):
                        return True
                return False
            else:
                c = ord(ele) - ord('a')
                if not node.children[c]:
                    return False
            
                node = node.children[c]
            i += 1
        return node.endWord

class Node:

    def __init__(self):
        self.children = [False] * 26
        self.endWord = False