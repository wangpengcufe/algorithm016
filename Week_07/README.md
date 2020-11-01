# 70.爬楼梯
#### 题目：https://leetcode-cn.com/submissions/detail/117150368/  70.爬楼梯 
#### 思路：动态方程dp，dp存的是结果，和num产生联系，即动态方程；当前台阶数等于前两节台阶数之和。
#### 遇到想要跳过 if n==0：continue的情况，可以直接把遍历范围从1开始遍历，1到n
```
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            dp[i+1] = dp[i-1] + dp[i]
        return dp[-1]
```

# 547 朋友圈
#### 题目：https://leetcode-cn.com/problems/friend-circles/  547
#### 思路：深度优先搜索，dfs；下标存的是朋友，下标10表示1和0的关系，下标01表示的是；数字存的是关系，1表示朋友，0表示不是朋友。
```
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
```

# 200 岛屿数量 
#### 题目：https://leetcode-cn.com/problems/number-of-islands/  
#### 思路：搜索，dfs
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i, j-1)
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count
```

# 22 括号生成
#### 题目：https://leetcode-cn.com/problems/generate-parentheses/ 
#### 思路：递归
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(left, right, tmp):
            if len(tmp) == 2 * n:
                result.append(tmp)
                return result
            if left < n:
                dfs(left + 1, right, tmp + '(')
            if right < left:
                dfs(left, right + 1, tmp + ')')
        dfs(0, 0, '')
        return result
```