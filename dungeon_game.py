"""

Dungeon Game

Solution
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

"""


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        r = len(dungeon) # rows
        c = len(dungeon[0]) # columns
        if not dungeon:
            return 0
        # dp matrix 
        dp = [[0]*c for _ in range(r)]  
        
        # base start case will be 
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        
        # right border first approach
        for j in range(c-1, 0, -1):
            dp[-1][j-1] = max(1, dp[-1][j] - dungeon[-1][j-1])
            
        for i in range(r-1, 0, -1):
            dp[i-1][-1] = max(1, dp[i][-1] - dungeon[i-1][-1])
        
        # will 1st 
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                dp[i][j] = min( max( 1, dp[i+1][j] - dungeon[i][j] ), max( 1, dp[i][j+1] - dungeon[i][j] ))    
                
        return dp[0][0]
        
# ================================================================        
# ================================================================
# ================================================================        

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0
        
        num_row, num_col = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * num_col
        dp[num_col - 1] = 1
        
        for row in reversed(range(num_row)):
            for col in reversed(range(num_col)):
                if row == num_row - 1 and col == num_col - 1:
                    dp[col] = max(1, 1 - dungeon[row][col])
                elif row == num_row - 1:
                    dp[col] = max(1, dp[col + 1] - dungeon[row][col])
                elif col == num_col - 1:
                    dp[col] = max(1, dp[col] - dungeon[row][col])
                else:
                    dp[col] = max(1, min(dp[col], dp[col + 1]) - dungeon[row][col])
        
        return dp[0]