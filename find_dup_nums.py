"""
Find the Duplicate Number

Solution
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[i:]:
                return nums[i]

class Solution:
    def findDuplicate(self, nums):
        s_nums = sorted(nums)
        # as we have sorted this will have duplicate items adjacent to each other
        for i in range(len(s_nums)-1):
            if s_nums[i] == s_nums[i+1]:
                return s_nums[i]
            

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            first = self.search_first_last(nums, i, True)
            second = self.search_first_last(nums, i, False)
            
            if second > first:
                return i
        return None
    
    # Returns the first or last index of element x in A 
    def search_first_last(self, A, x, is_first):
        lo = 0
        hi = len(A) - 1
        res = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if A[mid] == x:
                res = mid
                if is_first:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif A[mid] > x:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res