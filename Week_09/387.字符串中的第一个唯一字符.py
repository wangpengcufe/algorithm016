��Ŀ��https://leetcode-cn.com/problems/first-unique-character-in-a-string/   387. �ַ����еĵ�һ��Ψһ�ַ�
˼·����ϣӳ��
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for i in range(len(s)):
            if dic.get(s[i]) == 1:
                return i 
        return -1
