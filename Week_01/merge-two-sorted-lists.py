"""
��������������ϲ�Ϊһ���µ� ���� �������ء���������ͨ��ƴ�Ӹ�����������������нڵ���ɵġ�
ʾ����

���룺1->2->4, 1->3->4
�����1->1->2->3->4->4

���ӣ�https://leetcode-cn.com/problems/merge-two-sorted-lists
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