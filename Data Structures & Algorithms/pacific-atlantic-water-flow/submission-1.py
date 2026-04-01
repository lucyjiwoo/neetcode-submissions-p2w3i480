class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Pacific: top row + left col
        for c in range(COLS):
            dfs(0, c, pacific)
        for r in range(ROWS):
            dfs(r, 0, pacific)

        # Atlantic: bottom row + right col
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res