"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

链接：https://leetcode-cn.com/problems/pascals-triangle
"""

class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        resultList =[[1],[1,1]]
        for i in range(2,numRows):
            temp = [1]
            for j in range(1,i):
                temp.append(resultList[i-1][j-1]+resultList[i-1][j])
            temp.append(1)
            resultList.append(temp)
        return resultList