import bisect


# This is not a good solution, you can reach O(len(tasks)) with simple calculation and iteration
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = [0 for i in range(26)]
        for task in tasks: 
            index = ord(task) - ord('A')
            task_count[index] += 1
        task_count.sort()

        insert_point = bisect.bisect_right(task_count, 0)
        if insert_point != 0 :
            task_count = task_count[insert_point:]

        units_of_work = 0
        while len(task_count) > 0:
            last_value = task_count[-1]
            len_task_count = len(task_count)

            if len_task_count >= n + 1:
                for i in range(-(n + 1), 0):
                    task_count[i] -= 1
                units_of_work += n + 1
                task_count.sort()
            else:
                for i in range(len_task_count):
                    task_count[i] -= 1
                
                units_of_work += len_task_count if task_count[-1] == 0 else n + 1

            insert_point = bisect.bisect_right(task_count, 0)
            if insert_point != 0 :
                task_count = task_count[insert_point:]

        return units_of_work


        
