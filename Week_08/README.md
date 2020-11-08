# LRU缓存机制
#### 题目：https://leetcode-cn.com/problems/lru-cache/   146. LRU缓存机制
#### 思路一：用结合了哈希表与双向链表的数据结构 OrderedDict
#### 思路二：通过哈希表辅以双向链表实现，用一个哈希表和一个双向链表维护所有在缓存中的键值对。
```
class LRUCache(collections.OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
```
#### 双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
#### 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。
```
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
```

# 合并区间
#### 题目：https://leetcode-cn.com/problems/merge-intervals/    56. 合并区间
#### 思路：按照区间左端点从小到大排序，比较栈顶区间和当前区间是否有交集；
#### 有交集，则将栈顶区间的右端点更新为当前可达的最大值；
#### 无交集，则将当前区间加入栈中；
#### 时间复杂度：O(NlogN)

```
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
```
# 位1的个数
#### 题目：https://leetcode-cn.com/problems/number-of-1-bits/ 191. 位1的个数
#### 思路：二进制中最低位的1会通过n-1操作消失，而比最低位1高的位不变，通过n&=n-1保留剩余高位的1及低位的0
#### 时间复杂度：O(1)
```
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            n&=n-1
            res+=1
        return res
```