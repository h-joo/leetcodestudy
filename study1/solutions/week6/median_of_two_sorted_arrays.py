# https://leetcode.com/problems/median-of-two-sorted-arrays/

# This is not a correct solution this takes O(n) --> the problem asks us to solve this in O(log(n + m))
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         new_arr = []
#         i, j = 0, 0
#         while True:
#             if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
#                 new_arr.append(nums1[i])
#                 i+= 1
#             elif j < len(nums2):
#                 new_arr.append(nums2[j])
#                 j+= 1
#             else:
#                 break
        
#         if len(new_arr) % 2 != 0:
#             return new_arr[len(new_arr)//2] 
#         else:
#             return (new_arr[len(new_arr)//2] + new_arr[len(new_arr)//2 - 1]) / 2


# This is also not a correct solution as this is bigger than O(log n + m)
# import bisect

# def median_unbalanced(arr, start, end, left_missing, right_missing, total_length):
#     if left_missing < right_missing:
#         return median(arr, start + right_missing - left_missing, end, total_length)

#     if left_missing > right_missing:
#         return median(arr, start, end - left_missing + right_missing, total_length)

#     return median(arr, start, end, total_length)

# def median(arr, start, end, length):
#     half = min((start + end) // 2, len(arr) - 1)
#     if length % 2 == 0:
#         return (arr[half] + arr[half-1])/2
#     return arr[half]
    
# def find_median(nums1, nums2):
#     x0 = y0 = 0
#     x1 = len(nums1)
#     y1 = len(nums2)

#     total_length = x1 + y1
#     search_nums2 = True
#     prev_x = (x0 + x1) // 2
#     prev_y = 0
#     find_value = nums1[prev_x]
#     while x1 - x0 + y1 - y0 > 4:
#         if x0 == x1:
#             return median_unbalanced(nums2, y0, y1, x0 + y0, total_length - x1 - y1, total_length)

#         if y0 == y1:
#             return median_unbalanced(nums1, x0, x1, x0 + y0, total_length - x1 - y1, total_length)

#         if search_nums2:
#             search_nums2 = False
#             find_value = nums1[prev_x]
#             result = bisect.bisect_right(nums2, find_value, y0, y1)

#             left_length = prev_x + result 
#             right_length = len(nums1) - prev_x - 1 + len(nums2) - result
#             if left_length == right_length:
#                 return find_value
#             if left_length < right_length:
#                 x0 = prev_x
#                 y0 = result
#             else:
#                 x1 = min(x1, prev_x + 1)
#                 y1 = min(y1, result + 1)
#             prev_y = (y0 + y1) // 2
#         else:
#             search_nums2 = True
#             find_value = nums2[prev_y]
#             result = bisect.bisect_right(nums1, nums2[prev_y], x0, x1)

#             left_length = prev_y + result
#             right_length = len(nums2)- prev_y - 1 + len(nums1) - result
#             if left_length == right_length:
#                 return find_value
#             if left_length < right_length:
#                 x0 = result
#                 y0 = prev_y
#             else:
#                 x1 = min(x1, result + 1)
#                 y1 = min(y1, prev_y + 1)
#             prev_x = (x0 + x1) // 2
#     arr = []
#     for i in range(x0, x1):
#         arr.append(nums1[i])
#     for i in range(y0, y1):
#         arr.append(nums2[i])
#     arr.sort()
#     return median_unbalanced(arr, 0, len(arr), x0 + y0, total_length - x1 - y1, total_length)


# I needed to refer the editorial section to use a fast-enough solution.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(k, nums1, start1, end1, nums2, start2, end2):
            if start1 == end1:
                return nums2[k - start1]
            if start2 == end2:
                return nums1[k - start2]

            mid1 = (start1 + end1) // 2
            mid2 = (start2 + end2) // 2

            if nums1[mid1] > nums2[mid2]:
                return findKthElement(k, nums2, start2, end2, nums1, start1, end1)

            if mid1 + mid2 < k:                    
                return findKthElement(k, nums1, mid1 + 1, end1, nums2, start2, end2)
            
            return findKthElement(k, nums1, start1, end1, nums2, start2, mid2)

        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            return (findKthElement(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2)) + findKthElement(total_len // 2 - 1, nums1, 0, len(nums1), nums2, 0, len(nums2))) / 2
        
        return findKthElement(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2))
