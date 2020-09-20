class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        dic = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
        re = []
        for i in range(0, k):
            re.append(dic.pop(0)[0])
        return re