# https://leetcode.com/problems/unique-binary-search-trees/description/

def num_trees_recursive(n, memoize):
    if n in memoize:
        return memoize[n]
    memoize_sum = 0
    for i in range(n):
        memoize_sum += num_trees_recursive(i, memoize) * num_trees_recursive(n - 1 - i, memoize)
    memoize[n] = memoize_sum
    return memoize_sum

class Solution:
    def numTrees(self, n: int) -> int:
        memoize = {0:1, 1:1}
        return num_trees_recursive(n, memoize)
