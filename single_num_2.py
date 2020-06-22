"""
Single Number II

Solution
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

"""


class Solution:
    def find_sum(self, nums):
        sum = 0
        for num in nums:
            sum += num
        
        return sum
        
    def singleNumber(self, nums):
        raw_sum = self.find_sum(nums)
        set_sum = self.find_sum( set(nums) )
        
        return (3*set_sum - raw_sum)//2
    


# ===========================================================
# ===========================================================
# ===========================================================    


The idea is similar to problem Single Number, but here we need to count each bit modulo 3. So, we

Iterate over all possible 32 bits and for each num check if this num has non-zero bit on position i with num & (1<<i) == (1<<i) formula.
We evaluate this sum modulo 3. Note, that in the end for each bit we can have either 0 or 1 and never 2.
Next, update our answer single with evaluated bit.
Finally, we need to deal with overflow cases in python: maximum value for int32 is 2^31 - 1, so if we get number more than this value we have negative answer in fact.
Complexity: time complexity is O(32n), which may be not fully honest linear, but is fine for the purpose of this problem. If we want just O(n) complexity, I think problem becomes not medium but hard. Space complexity here is O(1).

class Solution:
    def singleNumber(self, nums):
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i) == (1<<i): count += 1
            single |= (count%3) << i
            
        return single if single < (1<<31) else single - (1<<32)   
        
