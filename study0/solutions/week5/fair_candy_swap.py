class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = 0
        bob_sum = 0
        bob_candies_idx = set()
        for i, candies in enumerate(aliceSizes):
            alice_sum += candies

        for i, candies in enumerate(bobSizes):
            bob_sum += candies
            bob_candies_idx.add(candies)
        
        diff = int((alice_sum - bob_sum)/2)

        for i, candies in enumerate(aliceSizes):
            if (candies - diff) in bob_candies_idx:
                return [candies, candies - diff]

