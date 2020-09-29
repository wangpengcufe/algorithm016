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