class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        # create frequency dictionary
        freq_dist = defaultdict(int)
        for letter in s:
            freq_dist[letter] += 1

        freq_sum = 0
        all_even_number = True
        for v in freq_dist.values():
            if v % 2 == 0:
                freq_sum += v
            else:
                all_even_number = False
                freq_sum += v - 1

        return freq_sum if all_even_number else freq_sum + 1
