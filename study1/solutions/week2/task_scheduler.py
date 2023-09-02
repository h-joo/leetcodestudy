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

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0 :
            return len(tasks)
        task_count = [0 for i in range(26)]
        for task in tasks: 
            task_count[ord(task) - ord('A')] += 1
        task_count = list(filter(lambda a: a!=0, task_count))
        task_count.sort()
        
        units_of_work = 0
        total_count = 0
        num_elems = len(task_count)
        while total_count < len(tasks):
            tasks_performed = 0
            i = num_elems - 1
            while i >= 0 and tasks_performed < n + 1:
                if task_count[i] == 0:
                    break
                task_count[i] -= 1
                tasks_performed += 1
                total_count += 1
                i -= 1

            for i in range(0, num_elems - 1):
                if task_count[i] > task_count[i+1]:
                    task_count[i], task_count[i+1] = task_count[i+1], task_count[i]
            
            task_count.sort()

            units_of_work += n + 1 if total_count < len(tasks) else tasks_performed
        return units_of_work
        
