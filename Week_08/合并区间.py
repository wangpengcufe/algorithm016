题目：https://leetcode-cn.com/problems/merge-intervals/    56. 合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        stack=[]
        n=len(intervals)
        intervals.sort()
        for i,interval in enumerate(intervals):
            left,right=interval
            if stack and stack[-1][1]>=left:
                stack[-1][1]=max(stack[-1][1],right)
            else:
                stack.append(interval)
        return stack