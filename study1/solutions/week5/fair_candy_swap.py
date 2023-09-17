# https://leetcode.com/problems/fair-candy-swap/

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = 0
        bob_sum = 0
        bob_candies = set()
        for candies in aliceSizes:
            alice_sum += candies

        for candies in bobSizes:
            bob_sum += candies
            bob_candies.add(candies)
        
        diff = int((alice_sum - bob_sum)/2)

        for candies in aliceSizes:
            if (candies - diff) in bob_candies:
                return [candies, candies - diff]
