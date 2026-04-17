class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] *len(temperatures)
        i = 0
        while i < len(temperatures):
            if not stack:
                stack.append((temperatures[i],i))
                i += 1
            else:
                if stack[-1][0] < temperatures[i]:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                else:
                    stack.append((temperatures[i],i))
                    i += 1

        return res


