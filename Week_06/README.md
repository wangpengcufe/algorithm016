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

# 最大正方形
#### 题目：https://leetcode-cn.com/problems/maximal-square/    最大正方形
#### 思路：使用dp[i][j]表示以matrix[i][j]为右下角的顶点的可以组成的最大正方形的边长。那么我们只需要计算所有的i，j组合，然后求出最大值即可
```
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]


        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else 0
                res = max(res, dp[i][j])
        return res ** 2
```

# 题目： https://leetcode-cn.com/problems/decode-ways   解码方法 
#### 思路： # dp[i]：以 s[i] 结尾的前缀字符串的解码个数
        #### 分类讨论：
        #### 1、s[i] != '0' 时，dp[i] = dp[i - 1]
        #### 2、10 <= s[i - 1..i] <= 26 时，dp[i] += dp[i - 2]
```
class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]
        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            num = 10 * (ord(s[i - 1]) - ord('0')) + (ord(s[i]) - ord('0'))
            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[size - 1]
```