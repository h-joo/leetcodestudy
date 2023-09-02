import queue

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        toVisit = queue.Queue()
        toVisit.put(root)
        while not toVisit.empty():
            current = toVisit.get()
            current.left, current.right = current.right, current.left
            if current.left is not None:
                toVisit.put(current.left)
            if current.right is not None:
                toVisit.put(current.right)
        return root