from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            nxt = node.children[char]

            if nxt.word:
                res.append(nxt.word)
                nxt.word = None  # avoid duplicates

            board[r][c] = "#"  # mark visited

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if board[nr][nc] != "#":
                        dfs(nr, nc, nxt)

            board[r][c] = char  # restore

            # optimization: prune leaf
            if not nxt.children:
                node.children.pop(char)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res