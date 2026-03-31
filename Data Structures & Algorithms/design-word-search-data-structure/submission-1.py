class TrieNode():
    def __init__(self):
        self.children = {}
        self.endofword = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endofword = True

    def search(self, word: str) -> bool:
        cur, i = self.root, 0
        def backtrack(cur, i):
            if i == len(word):
                return cur.endofword
            if word[i] not in cur.children:
                if word[i] == ".":
                    childs = cur.children.keys()
                    for c in childs:
                        if backtrack(cur.children[c], i + 1):
                            return True
            else:
                if backtrack(cur.children[word[i]], i +1):
                    return True
            return False
        return backtrack(cur, i)

