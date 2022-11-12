# https://leetcode.com/problems/unique-binary-search-trees/description/

def num_trees_recursive(num_nodes, memoize):
    if num_nodes in memoize:
        return memoize[num_nodes]
    memoize_sum = 0
    for i in range(num_nodes):
        memoize_sum += num_trees_recursive(i, memoize) * num_trees_recursive(num_nodes - 1 - i, memoize)
    memoize[num_nodes] = memoize_sum
    return memoize_sum

class Solution:
    def numTrees(self, n: int) -> int:
        memoize = {0:1, 1:1}
        return num_trees_recursive(n, memoize)
