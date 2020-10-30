题目：https://leetcode-cn.com/problems/friend-circles/  547
思路：深度优先搜索，dfs；下标存的是朋友，下标10表示1和0的关系，下标01表示的是；数字存的是关系，1表示朋友，0表示不是朋友。
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        visited = [0] * len(M)
        def dfs(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(M, visited, j)
        for i in range(len(M)):
            if not visited[i]:
                dfs(M, visited, i)
                count += 1
        return count 