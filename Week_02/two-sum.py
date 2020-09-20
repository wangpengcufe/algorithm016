class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic.keys():
                return [dic.get(target - nums[i]), i]
            else:
                dic[nums[i]] = i 
        return []