题目： https://leetcode-cn.com/problems/task-scheduler/
思路：完成所有任务的最短时间取决于出现次数最多的任务数量。
1、计算每个任务出现的次数
2、找出出现次数最多的任务，假设出现次数为 x
3、计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
4、计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        
        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length