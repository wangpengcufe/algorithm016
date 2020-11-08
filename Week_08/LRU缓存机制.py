��Ŀ��https://leetcode-cn.com/problems/lru-cache/   146. LRU�������
˼·��һ���ý���˹�ϣ����˫����������ݽṹ OrderedDict
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
˼·����ͨ����ϣ����˫������ʵ�֣���һ����ϣ���һ��˫������ά�������ڻ����еļ�ֵ�ԡ�
˫�������ձ�ʹ�õ�˳��洢����Щ��ֵ�ԣ�����ͷ���ļ�ֵ�������ʹ�õģ�������β���ļ�ֵ�������δʹ�õġ�
��ϣ��Ϊ��ͨ�Ĺ�ϣӳ�䣨HashMap����ͨ���������ݵļ�ӳ�䵽����˫�������е�λ�á�
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # ʹ��αͷ����αβ���ڵ�    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # ��� key ���ڣ���ͨ����ϣ��λ�����Ƶ�ͷ��
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # ��� key �����ڣ�����һ���µĽڵ�
            node = DLinkedNode(key, value)
            # ��ӽ���ϣ��
            self.cache[key] = node
            # �����˫�������ͷ��
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # �������������ɾ��˫�������β���ڵ�
                removed = self.removeTail()
                # ɾ����ϣ���ж�Ӧ����
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # ��� key ���ڣ���ͨ����ϣ��λ�����޸� value�����Ƶ�ͷ��
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