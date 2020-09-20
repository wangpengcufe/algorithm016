
- 1. 如果一个链表有多个指针的话就变成了树
- 2. 二叉树的时间复杂度是log n
- 3. 树的面试解法一般都是递归，原因，树没有后继和循环的结构，只有左右节点
- 4. 每个节点的定义代码，总结
- 5. 前中后序的遍历代码，总结
- 6. 完全二叉树，叶子节点都是满的。
- 7. 二叉堆的索引总结
- 8. 堆的插入操作：先加到队尾，然后调整位置。

- 关于树的前中后序遍历的方法：

```
# 每个节点的定义代码
class TreeNode:
	def __init__(self, val):
    	self val = val
		self left, self.right = None, None

# 前中后序的遍历代码
	def preorder(self, root):
		if root:
			self traverse_path.append(root.val)
			self.preorder(root.left)
			self.preorder(root.right)

	def inorder(self, root):
		if root:
			self.inorder(root.left)
			self.traverse_path.append(root.val)
			self.inorder(root.right)

	def postorder(self, root):
		if root:
			self.postorder(root.left)
			self.postorder(root.right)
			self.traverse_path.append(root.val)
	
	# 二叉堆的索引总结
	根节点（顶堆元素）是 a[0]
	1.索引为i的左孩子的索引是 （2*i +1）
	2.索引为i的右孩子的索引是（2*i +2）
	3.索引为i的父节点的索引是 floor((i -1)/2)
```

- 链表的常用方法：
 - LinkedList() ：创建空链表，不需要参数，返回值是空链表；
 - is_empty()：测试链表是否为空，不需要参数，返回值是布尔值；
 - append(data) ：追加元素到链表尾部。参数是要追加的元素，无返回值；
 - iter()：生成器，遍历链表，无参数，无返回值；
 - insert(idx, value) ：插入一个元素，参数为插入元素的索引和值；
 - remove(idx)：移除1个元素，参数为要移除的元素或索引，并修改链表；
 - size() ：返回链表的元素数，不需要参数，返回值是个整数；
 - search(item) ：查找链表某元素，参数为要查找的元素或索引，返回是布尔值。

- 关于队列用法的总结：
 - 1、deque其实是 double-ended queue 的缩写，翻译过来就是双端队列。
 - 2、最大的好处就是实现了从队列头部快速增加和取出对象: .popleft(), .appendleft()
 - 3、list对象的这两种用法的时间复杂度是 O(n) ，也就是说随着元素数量的增加耗时呈线性上升
 - 4、使用deque对象则是 O(1) 的复杂度，所以当你的代码有这样的需求的时候， 一定要记得使用deque
 - 5、deque还提供了一些其他的好用方法，比如 rotate（旋转）
 - 6、from collections import deque
 - 7、deque: 双端队列，可以快速的从另外一侧追加和推出对象
 - 8、list.pop(0) 正确，弹出第0个位置的元素
 - 9、deque.pop(0) 错误，无法弹出带参数的情况；  deque.pop() 正确，弹出最后一个元素，右边队尾为最后一个元素
 - 10、list.popleft() 错误，list没有 popleft方法；  list.appendleft()错误， list没有appendleft方法
