"""
���ʵ��˫�˶��С�
���ʵ����Ҫ֧�����²�����

MyCircularDeque(k)�����캯��,˫�˶��еĴ�СΪk��
insertFront()����һ��Ԫ����ӵ�˫�˶���ͷ���� ��������ɹ����� true��
insertLast()����һ��Ԫ����ӵ�˫�˶���β������������ɹ����� true��
deleteFront()����˫�˶���ͷ��ɾ��һ��Ԫ�ء� ��������ɹ����� true��
deleteLast()����˫�˶���β��ɾ��һ��Ԫ�ء���������ɹ����� true��
getFront()����˫�˶���ͷ�����һ��Ԫ�ء����˫�˶���Ϊ�գ����� -1��
getRear()�����˫�˶��е����һ��Ԫ�ء�?���˫�˶���Ϊ�գ����� -1��
isEmpty()�����˫�˶����Ƿ�Ϊ�ա�
isFull()�����˫�˶����Ƿ����ˡ�
ʾ����

MyCircularDeque circularDeque = new MycircularDeque(3); // ����������СΪ3
circularDeque.insertLast(1);			        // ���� true
circularDeque.insertLast(2);			        // ���� true
circularDeque.insertFront(3);			        // ���� true
circularDeque.insertFront(4);			        // �Ѿ����ˣ����� false
circularDeque.getRear();  				// ���� 2
circularDeque.isFull();				        // ���� true
circularDeque.deleteLast();			        // ���� true
circularDeque.insertFront(4);			        // ���� true
circularDeque.getFront();				// ���� 4

��ʾ��

����ֵ�ķ�ΧΪ [1, 1000]
���������ķ�ΧΪ [1, 1000]
�벻Ҫʹ�����õ�˫�˶��п⡣

���ӣ�https://leetcode-cn.com/problems/design-circular-deque
"""

class MyCircularDeque:
    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.arr = [0 for _ in range(self.capacity)]
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity;
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]
    def isEmpty(self) -> bool:
        return self.front == self.rear
    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front