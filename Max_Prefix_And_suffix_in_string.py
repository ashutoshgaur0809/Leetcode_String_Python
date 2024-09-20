s = "ababab"


# prefix list
pl = []
for i in range(1,len(s)):
    pl.append(s[0:i])
print("Prefix List -> ",pl)

# SUFFIX list
sl = []
for i in range(1,len(s)):
    sl.append(s[i:])
print("Suffix List -> ",sl)

# Find same prefix and suffix 
nl = []
for i in pl:
    if i in sl:
        nl.append(i)

# find the maxed len prefix and suffix
maxi = 0
ans = ""
for i in nl:
    
    n = len(i)
    if n > maxi:
        ans = i  
        
        
print(nl)
print(ans)


# Approach 2
        longest = ""

        # Check for common prefixes and suffixes directly
        for i in range(1, len(s)):
            prefix = s[:i]  # Current prefix
            suffix = s[-i:]  # Current suffix
            if prefix == suffix:
                longest = prefix 

              
# Example 1:

# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
# Example 2:

# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
