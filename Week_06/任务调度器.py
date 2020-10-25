��Ŀ�� https://leetcode-cn.com/problems/task-scheduler/
˼·�����������������ʱ��ȡ���ڳ��ִ�����������������
1������ÿ��������ֵĴ���
2���ҳ����ִ����������񣬼�����ִ���Ϊ x
3������������Ҫ��ʱ�� (x - 1) * (n + 1)����Ϊ min_time
4��������ִ���Ϊ x ���������� count���������ս��Ϊ min_time + count

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        
        # ���ڼ�¼ÿ��������ֵĴ���
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # ��������ֵĴ����Ӵ�С����
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
        # ������������Ĵ���
        max_task_count = task_sort[0][1]
        # ������Ҫ�����ʱ��
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        # �����������������٣��򷵻���������
        return res if res >= length else length