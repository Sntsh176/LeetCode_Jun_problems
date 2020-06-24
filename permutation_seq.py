"""
Permutation Sequence

Solution
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


# here will do simple thing as detailed below
"""n=6, k=314. How we can find the first digit? There are 5! = 120 permutations, 
which start with 1, there are also 120 permutations, which start with 2 ( d = factor) , 
and so on. 314 > 2*120 and 314 < 3*120, so it means, that the fist digit we need to take is 3

k = 314-2*5! = 74, n - 1 = 5, d = 3, build number so far 3, digits = [1,2,4,5,6]
k = 74-3*4! = 2, n - 1 = 4, d = 0, build number so far 35, digits = [1,2,4,6]
k = 2-0*3! = 2, n - 1 = 3, d = 0, build number so far 351, digits = [2,4,6]
k = 2-1*2! = 0, n - 1 = 2, d = 2, build number so far 3512, digits = [4,6]
k = 0-1*1! = 0, n - 1 = 1, d = 2, build number so far 35126, digits = [4]
Finally, we have only one digit left, output is 351264.

"""
class Solution:
    def get_factorial(self, n):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
        
    def getPermutation(self, n: int, k: int) -> str:
    
        # let's create one simple list with the numbers [ 1,2,3 ....9] if n = 9
        nums = [i for i in range(1, n+1)]
        # now will define answer initially as blank string
        ans = ""
        
        # will try to find the factor ( d ) for which the (n-1) factorial will be within k
        # initial permutation is indexed 0 -  indexing is starting from 0, so k = k - 1 to get correct output
        k = k - 1 
        
        for _ in range(n):
            f = self.get_factorial(n-1)
            d = k // f
            # now we have 1st letter at d index will decrement n and remainder will be modified k
            k = k % f
            
            n = n-1
            
            ans += str(nums[d])
            # we have selected the letter then will remove it 
            nums.pop(d)
            
        return ans
        
# ===================================================================        
# ===================================================================
# ===================================================================
        
class Solution(object):
    def get_factorial(self, n):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    def getPermutation(self, n, k):
        # * the symbols that will be permuted
        chars = [str(i) for i in range(1, n + 1)]
        # * total number of permutations for this n
        k -= 1  # * change indexing to 0
        permutations = self.get_factorial(n)
        result = []

        while chars:
            # * get the first digit (range is 0 to n-1)
            digit = n * k // permutations
            result.append(chars[digit])  # * map from digit to a symbol
            del chars[digit]  # * remove that symbol
            # * repeat for next digit with decreased permutations, n and k
            permutations //= n
            k -= digit * permutations
            n -= 1

        return "".join(result)
        