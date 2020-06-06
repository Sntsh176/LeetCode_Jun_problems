"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""


class Solution:

    def __init__(self, w: List[int]):
        self.w = w[:]
        # here we are creating another list which will be having accumalative sum
        # eg. given [4,2,1] => [4,6,7]
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1] 

    def pickIndex(self) -> int:
        # now here will implement the random functionality
        # generate a random number in the range of 1, max        
        # Now this random number needs to be searched and willr return the index of it
        # let's do with binary search
        idx = random.randint(1, self.w[-1])
        ans, lo, hi = -1, 0, len(self.w) - 1
        while lo <= hi:
            md = lo + (hi - lo) // 2
            if self.w[md] >= idx:
                ans = md
                hi = md - 1
            else:
                lo = md + 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()