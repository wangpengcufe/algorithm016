"""
����һ���������������������ڵĽڵ㣬�����ؽ����������

�㲻��ֻ�ǵ����ĸı�ڵ��ڲ���ֵ��������Ҫʵ�ʵĽ��нڵ㽻����

ʾ��:

���� 1->2->3->4, ��Ӧ�÷��� 2->1->4->3.

���ӣ�https://leetcode-cn.com/problems/swap-nodes-in-pairs
"""

class Solution(object):
    def swapPairs(self, head):
        h = ListNode(-1)
        h.next = head
        pre = h
        while pre.next != None and pre.next.next != None:
            node1 = pre.next
            node2 = node1.next
            lat = node2.next
            pre.next = node2            
            node2.next = node1
            node1.next = lat 
            pre = node1
        return h.next