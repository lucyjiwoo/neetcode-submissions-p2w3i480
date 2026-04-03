class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            pre[a].append(b)

        visiting = set()
        visited = set()
    
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for rc in pre[course]:
                if not dfs(rc):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

