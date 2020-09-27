# 三数之和
#### 思路：排序+双指针法， O（n^2）
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        re = []
        for i in range(len(nums)):
            L, R = i + 1, len(nums) -1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while L < R :
                if nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else: 
                    re.append([nums[i], nums[L], nums[R]])
                    while L<R and nums[L] == nums[L+1]:
                        L +=1
                    while L<R and nums[R] == nums[R-1]:
                        R -=1
                    L += 1
                    R -= 1
        return re
```


# 第k个数
### 思路:三指针法 O(n)
```
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        num3 = num5 = num7 = 0
        lis = [1]
        for i in range(k):
            temp = min(lis[num3]*3, lis[num5]*5, lis[num7]*7)
            lis.append(temp)
            if temp == lis[num3]*3:
                num3 += 1
            if temp == lis[num5]*5:
                num5 += 1
            if temp == lis[num7]*7:
                num7 += 1
        return lis[k-1]
```