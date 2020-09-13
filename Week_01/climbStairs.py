"""
������������¥�ݡ���Ҫ n?������ܵ���¥����

ÿ��������� 1 �� 2 ��̨�ס����ж����ֲ�ͬ�ķ�����������¥���أ�

ע�⣺���� n ��һ����������

ʾ�� 1��
���룺 2
����� 2
���ͣ� �����ַ�����������¥����
1.  1 �� + 1 ��
2.  2 ��

ʾ�� 2��
���룺 3
����� 3
���ͣ� �����ַ�����������¥����
1.  1 �� + 1 �� + 1 ��
2.  1 �� + 2 ��
3.  2 �� + 1 ��

���ӣ�https://leetcode-cn.com/problems/climbing-stairs
"""
class Solution(object):
    def climbStairs(self, n):
        f0 = 0
        f1 = 1
        f2 = 2
        if n<=0:
            return f0
        elif n==1:
            return f1
        elif n==2:
            return f2
        else:
            result = 0
            for i in range(3,n+1):
                result = f1+f2
                f1 = f2
                f2 = result
        return result