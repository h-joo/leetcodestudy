import bisect

def leastInterval(tasks, n):
    task_queue = [0 for i in range(26)]
    for task in tasks: 
        index = ord(task) - ord('A')
        task_queue[index] += 1
    task_queue.sort()

    insert_point = bisect.bisect_right(task_queue, 0)
    if insert_point != 0 :
        task_queue = task_queue[insert_point:]

    units_of_work = 0
    while len(task_queue) > 0:
        first_value = task_queue[0]
        num_task_queue = len(task_queue)
        print(task_queue)
        for i in range(num_task_queue):
            task_queue[i] -= first_value
        insert_point = bisect.bisect_right(task_queue, 0)
        if insert_point != 0 :
            task_queue = task_queue[insert_point:]
        
        if num_task_queue >= n + 1:
            units_of_work += num_task_queue * first_value
        else:
            if len(task_queue) == 0:
                units_of_work += (n + 1) * (first_value - 1)
                units_of_work += num_task_queue
            else:
                units_of_work += (n + 1) * first_value

    return units_of_work

leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)