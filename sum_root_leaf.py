"""

Sum Root to Leaf Numbers

Solution
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total_sum = 0
        # will use recursive function to call child node till reached to the leaf node
        def dfs(node, total_sum):
            # check if it is leaf node or not
            if not node:
                return 0
                
            # at each depth the value gets 10 multiple and sum should be created (in STR type number will created by adding it)
            total_sum = total_sum*10 + node.val
            if not node.left and not node.right:
                return total_sum
                # as we have reached the leaf node
            
            return dfs(node.left, total_sum) + dfs(node.right, total_sum)
        
        return dfs(root, total_sum)