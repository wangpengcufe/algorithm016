��Ŀ��https://leetcode-cn.com/problems/reverse-words-in-a-string/ 151. ��ת�ַ�����ĵ���
˼·��split, reverse, join, O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        return ' '.join(arr)