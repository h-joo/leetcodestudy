def parse_input():
    test_cases = [] 
    for _ in range(int(input())):
        test_cases.append(list(map(int, input().split())))
    return test_cases

def solution():
    for i, test_case in enumerate(parse_input()):
        print("Case #{}: {}".format(i+1, solve(test_case)))
        
def solve(test_case):
    num_levels, current_level, sword_level = test_case
    return_approach = current_level - sword_level + num_levels - sword_level
    return current_level + min(return_approach, num_levels)
    
solution()
