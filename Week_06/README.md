# 最小路径和
#### 题目：https://leetcode-cn.com/problems/minimum-path-sum
#### 思路：动态规划，dp存储的是结果，和num产生联系，即动态方程，O（n^2）
```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dp = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][j-1]
                elif j == 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
```

# 回文字串
#### 题目：https://leetcode-cn.com/problems/palindromic-substrings/   647
#### 思路：动态规划dp,字符串s[i?j]是否为回文子串，如果是，dp[i][j]=true，
#### 如果不是, dp[i][j]=false。考虑base case，这里显而易见，当只有一个字母的时候肯定是回文子串。
#### 为什么从右下角遍历：因为在填dp表时，(i, j) 位置的值依赖于（i+1,j-1），
#### 也就是当前位置的左下方。显然如果从上往下遍历，左下方的值就完全没有初始化，
#### 当然当前位置也会是错误的。但是从右下角遍历就保证了左下方的所有值都已经计算好了。
```
class Solution:
    def countSubstrings(self, s: str) -> int:
        if s is None or s == "":
            return 0
        n = len(s)

        dp = [[False for i in range(n)] for j in range(n)]
        result = len(s)

        for i in range(n):
            # base case: 只有一个字母的时候肯定是回文子串
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    result += 1
        return result
```