def parse_test_cases():    
    test_cases = []
    for _ in range(int(input())):
        test_cases.append((input(), input()))
    return test_cases

def get_left(i):
    return i - 1 if i != 0 else 25

def get_right(i):
    return i + 1 if i != 25 else 0


def mark_distance(favorite_diff_lookup, left, right):
    distance = 1
    while True:
        favorite_diff_lookup[left] = distance
        favorite_diff_lookup[right] = distance
        if left == right or get_right(left) == right:
            break
        left = get_right(left)
        right = get_left(right)
        distance += 1

def solve_one_problem(padlock, favorite):
    favorite_diff_lookup = [-1] * 26
    
    for char in favorite:
        favorite_diff_lookup[ord(char) - ord('a')] = 0
    
    if len(favorite) == 1:
        i = ord(favorite[0]) - ord('a')
        mark_distance(favorite_diff_lookup, get_right(i), get_left(i))
        return sum([favorite_diff_lookup[ord(char) - ord('a')] for char in padlock])

    for char in favorite:
        i = ord(char) - ord('a')

        left_left = left_right = get_left(i)
        if favorite_diff_lookup[left_left] == -1:
            while favorite_diff_lookup[left_left] != 0:
                left_left = get_left(left_left)
            left_left = get_right(left_left)
            mark_distance(favorite_diff_lookup, left_left, left_right)
    
        right_left = right_right = get_right(i)
        if favorite_diff_lookup[right_right] == -1:
            while favorite_diff_lookup[right_right] != 0:
                right_right = get_right(right_right)        
            right_right = get_left(right_right)
            mark_distance(favorite_diff_lookup, right_left, right_right)

            
    return sum([favorite_diff_lookup[ord(char) - ord('a')] for char in padlock])
    

def solution():
    for i, test_case in enumerate(parse_test_cases()):
        padlock, favorite = test_case
        print("Case #{}: {}".format(i + 1, solve_one_problem(padlock, favorite)))
        
solution()
