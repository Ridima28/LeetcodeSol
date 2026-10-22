# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:


        if root is None:
            return 
        ans = []
        queue = deque([root])
        while queue:
            level_sum = 0
            for i in range(len(queue)):
                node  = queue.popleft()
                level_sum += node.val

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

            ans.append(level_sum)

        if k > len(ans):
            return -1

        ans.sort(reverse=True)

        return ans[k-1]