��Ŀ��https://leetcode-cn.com/problems/friend-circles/  547
˼·���������������dfs���±��������ѣ��±�10��ʾ1��0�Ĺ�ϵ���±�01��ʾ���ǣ����ִ���ǹ�ϵ��1��ʾ���ѣ�0��ʾ�������ѡ�
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        visited = [0] * len(M)
        def dfs(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(M, visited, j)
        for i in range(len(M)):
            if not visited[i]:
                dfs(M, visited, i)
                count += 1
        return count 