# 柠檬水找零
### 思路：贪心算法，双指针
```
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num5 = num10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                num5 += 1
            elif bills[i] == 10:
                if num5 > 0:
                    num5 -= 1
                    num10 +=1
                else:
                    return False 
            else:
                if num5 >=1 and num10 >= 1:
                    num5 -= 1
                    num10 -=1
                elif num5 >=3:
                    num5 = num5 - 3
                else:
                    return False
        return True
```

# 买卖股票的最佳时机II
### 思路：贪心法，直接比较当前元素和前一个元素
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            if i >0 and prices[i-1] < prices[i]:
                result += (prices[i] - prices[i-1])
        return result
```