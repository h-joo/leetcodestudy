# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for string in strs:
            grouped_anagrams["".join(sorted(string))].append(string)
        
        return grouped_anagrams.value()
