"""
ou are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

"""



# Explanation

"""
Let dp_sum[i][j] be a number of ways to represent amount i such that we use only first j coins. We initialize the first column of this table with 1, because we can say there is one way to get amount = 0, using first j coins: do not take any coins.
To find dp_sum[i][j] we need to look at the last coin taken, it consists of two terms:

dp_sum[i][j-1], number of options, where we take only first j-1 coins
dp_sum[i-coins[j]][j], number of options, where we removed coin number j and we need to find number of options for the rest amount.
Example: let us consider coins = [1,2,5] and amont = 5. Then table dp_sum will be equal to

0	1	2	3	4	5
coin #0 (1)	1	1	1	1	1	1
coin #1 (2)	1	1	2	2	3	3
coin #2 (5)	1	1	2	2	3	4
Complexity is O(amount *N), where N is number of different coins, because we need only O(1) to update each cell.

In code I use index i+1 instead of i, because we start from 1st column, not 0th.

"""

# Here we have used 1D list as here as part of Dynamic Programming we have to use last row value 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # here will create the DP list , 2D array
        dp = [0]*(amount+1)
        dp[0] = 1
        # we set 1st one as 1
        
        for c in coins:
            for x in range(c, amount+1):
                dp[x] += dp[x-c]
                
        return dp[-1]