# https://leetcode.com/problems/sliding-window-maximum/description/

import heapq
# 1500 ms
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        occurances = defaultdict(int)
        queue = []
        for i in range(k):
            if nums[i] not in occurances:
                heapq.heappush(queue, -nums[i])
            occurances[nums[i]] += 1

        max_window = [-queue[0]]
        before, left, right = 0, 1, k

        while right < len(nums):
            to_delete = nums[before]
            to_add = nums[right]
            occurances[to_delete] -= 1
    
            if occurances[to_delete] == 0 and -queue[0] == to_delete:
                while len(queue) > 0 and occurances[-queue[0]] == 0:
                    heapq.heappop(queue)

            occurances[to_add] += 1

            if occurances[to_add] == 1:
                heapq.heappush(queue, -to_add)

            max_window.append(-queue[0])
            before += 1
            left += 1
            right += 1
        return max_window 
      
#########################################################################
import bisect

# 4500 ms
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sorted_list = [nums[i] for i in range(k)]
        sorted_list.sort()

        max_window = [sorted_list[-1]]
        before, left, right = 0, 1, k

        while right < len(nums):
            to_delete = nums[before]
            to_add = nums[right]

            del_idx = bisect.bisect_right(sorted_list, to_delete)
            del sorted_list[del_idx - 1]            
            add_idx = bisect.bisect_right(sorted_list, to_add)
            sorted_list.insert(add_idx, to_add)

            max_window.append(sorted_list[-1])
            before += 1
            left += 1
            right += 1
        return max_window        