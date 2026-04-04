class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node: int) -> None:
            if node in visited:
                return
            
            visited.add(node)
            
            for nei in graph[node]:
                dfs(nei)

        count = 0
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count
        