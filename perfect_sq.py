"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""


class Solution:
    def numSquares(self, n: int) -> int:
        # will use dynamic programming 
        dp = [0]*(n+1)
        
        for x in range(1, n+1):
            min_val = x
            y, sq = 1,1
            while sq <= x:
                min_val = min(min_val, 1+dp[x-sq])
                y += 1
                sq = y*y
                
            dp[x] = min_val
            
        return dp[n]
        
        

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]