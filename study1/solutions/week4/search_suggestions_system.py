# https://leetcode.com/problems/search-suggestions-system/

import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        last_insert_point = 0
        prefix = ''
        for ch in searchWord:
            prefix += ch
            last_insert_point = bisect.bisect_left(products, prefix, last_insert_point)
            match = []
            for i in range(last_insert_point, min(len(products), last_insert_point + 3)):
                if not products[i].startswith(prefix):
                    break
                match.append(products[i])
            result.append(match)

        return result