# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            self.total = 1 # initialised count with root node 
            
        def recur_call(node):
            if not node:
                return
            if node.left:
                self.total += 1
                recur_call(node.left)
            if node.right:
                self.total += 1
                recur_call(node.right)
                
        recur_call(root) # this will call the recusive function and inplace count will get increment as instance variable
        return self.total
        

# ============================================================        
# ============================================================          
# ============================================================  


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ld = self.get_depth(root.left)
        rd = self.get_depth(root.right)
        if ld == rd:
            return 2 ** ld + self.countNodes(root.right)
        return 2 ** rd + self.countNodes(root.left)

    def get_depth(self, node):
        if node is None:
            return 0
        return 1 + self.get_depth(node.left)