# Sol 1
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        new_s = s + "#" + rev_s
        
        # KMP table for the concatenated string
        n = len(new_s)
        lps = [0] * n
        
        # Build the KMP table (lps array)
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j
        
        # The length of the longest palindromic prefix is given by the last value in the lps array
        to_add = rev_s[:len(s) - lps[-1]]  # characters to add in front of the original string
        return to_add + s

# Sol2
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i=0
        ans=0
        for j in range(len(s)):
            st = s[i:j+1]
            pl = st[::-1]
            if st==pl:
                ans=j
        print(ans)
        k=s[ans+1:]
        k=k[::-1]
        return k+s


# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
