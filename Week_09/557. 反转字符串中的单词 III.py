��Ŀ��https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/   557. ��ת�ַ����еĵ��� III
˼·��split, ���ʷ�ת��join�� �ַ�����ת�� O��n��
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]