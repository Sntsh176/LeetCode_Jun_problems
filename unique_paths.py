"""

Unique Paths

Solution
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # here we will be using dynamic programming 
        dp = [[1]*n for _ in range(m)]
        # we have intialized the min path to 1 as we have atleast one path
        # and for every cell we can either come from left or top so path will = left path + top path
        
        for r in range(1, m):
            for c in range(1, n):
                # will fetch path from previous records ( left + top)
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        return dp[-1][-1]
        