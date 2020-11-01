题目：https://leetcode-cn.com/problems/generate-parentheses/ 括号生成
思路：递归

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