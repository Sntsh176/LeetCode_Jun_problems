"""

Longest Duplicate Substring

Solution
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
   Hide Hint #1  
Binary search for the length of the answer. (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
   Hide Hint #2  
To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.


"""



class Solution:
    # defining Method based on the Robin Karp Algo
    def robin_karp(self, S_text, M, Q):
    
        # calculating hash values
        rolling_hash = 0
        power_last = pow(26, M, Q)
        # here 26 is base as we are dealing with 26 char alphabet
        
        for i in range(M):
            rolling_hash = (rolling_hash * 26 + ord(S_text[i])) % Q
            
        # creating a set which will be having all the seen entries
        seen = {rolling_hash}
        
        for i in range(M, len(S_text)):
                rolling_hash = (rolling_hash * 26 + ord(S_text[i]) - power_last * ord(S_text[i - M])) % Q
                
                # Now will check in existing
                if rolling_hash in seen:
                    return i-M+1
                else:
                    seen.add(rolling_hash)
                    
        return -1
    
    def longestDupSubstring(self, S: str) -> str:
        # Let's do it , will apply binary search to find the part of the text to be checked for duplicates
        l = 0
        r = len(S)-1
        
        # initializing the values for Robin-Karp Algo
        res = 0
        q = (1 << 63) - 1
        # just to get mod as a higher num needed as per algo
        
        # applying the Binary Search
        while l < r:
            m = (l+r+1) // 2
            # calling robin-karp method
            is_valid = self.robin_karp(S, m, q)
            
            if is_valid != -1:
                # find the duplicate string with length mid
                l = m
                res = is_valid
            else:
                r = m-1
                
        return S[res:res+l]
        