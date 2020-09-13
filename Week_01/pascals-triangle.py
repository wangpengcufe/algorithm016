"""
����һ���Ǹ����� numRows������������ǵ�ǰ numRows �С�

����������У�ÿ�����������Ϸ������Ϸ������ĺ͡�

ʾ��:

����: 5
���:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

���ӣ�https://leetcode-cn.com/problems/pascals-triangle
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