"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
"""
class Solution(object):
    def mergeTwoLists(self, l1, l2):
       if not l1 : return l2
       if not l2 : return l1
       if l1.val <= l2.val:
           l1.next = self.mergeTwoLists(l1.next, l2)
           return l1
       else:
           l2.next = self.mergeTwoLists(l1, l2.next)
           return l2