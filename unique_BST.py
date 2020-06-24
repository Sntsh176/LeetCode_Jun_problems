"""
Unique Binary Search Trees

Solution
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
   
"""
   
class Solution:
    def numTrees(self, n: int) -> int:
        # here will use the DP approach
        # will reuse the previously calculated values to find the next n BST count
        if n == 0 or n == 1:
            return 1
            
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1 # as above 1st line value intiated
        
        for i in range(2, n+1):
            for j in range(i):
                
                dp[i] += dp[j] * dp[i-j-1]
                
        return dp[-1]
        
# CATALAN NUMBER (2n)!/((n+1)!*n!)  ##
# math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))