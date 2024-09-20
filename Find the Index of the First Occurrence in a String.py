class Solution:
    def strStr(self, h: str, n: str) -> int:

        if h == n:
            return 0
        l = []
        k = len(n)
        for i in range(0,len(h)):
            l.append(h[i:i+k])
        
        for i in range(len(l)):
            if n in l[i]:
                return i
        
        return -1

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
