"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000

"""


"""
Let us first send all the people to the first city. Now, we need to choose half of them and change their city from first to second. Which ones we need to choose? Obviously the half with the smallest difference of costs between second and first cities. This difference can be negative and positive. Let us go through example: costs = [[10,20],[30,200],[400,50],[30,20]]
Then:

We put all of them to 1 city and pay 10 + 30 + 400 + 30
Now, evaluate differences: 10, 170, -350, -10.
Choose 2 smallest differences, in this case it is -350 and -10 (they are negative, so we can say we get a refund)
Evaluate final sum as 10 + 30 + 400 + 30 + -350 + -10 = 110
Complexity is O(n log n), because we need to make one sort, and O(n) for evaluating differences and two sums. Space complexity is O(n), because we need to keep array of differences.
"""


class Solution:
    def twoCitySchedCost(self, costs):
        FirstCity = [i for i,j in costs]
        Diff = [j - i for i,j in costs]
        return sum(FirstCity) + sum(sorted(Diff)[:len(costs)//2])
        
# =================================================================
# =================================================================
        
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        n = len(costs)

        
        return sum(costs[i][0] for i in range(n//2)) + sum(costs[i][1] for i in range(n//2,n))