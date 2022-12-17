def parse_test_cases():
    test_cases = []
    for _ in range(int(input())):
        input()
        test_cases.append(list(map(int, list(input()))))
    return test_cases
    
def solve_one_problem(lst):
    distance_array = [-1] * len(lst)
    for i in range(len(lst)):
        if lst[i] == 0:
            continue
        left, right = i - 1, i + 1
        left_distance, right_distance = 1, 1
        while left >= 0 and lst[left] == 0 and (distance_array[left] > left_distance or distance_array[left] == -1):
            distance_array[left] = left_distance
            left_distance += 1
            left -= 1
            
        while right < len(lst) and lst[right] == 0 and (distance_array[right] > right_distance or distance_array[right] == -1):
            distance_array[right] = right_distance
            right_distance += 1
            right += 1
            
        distance_array[i] = 0
    return sum(distance_array)
    

def solve():
    for i, test_case in enumerate(parse_test_cases()):
        print("Case #{}: {}".format(i+1, solve_one_problem(test_case)))
        
solve()

