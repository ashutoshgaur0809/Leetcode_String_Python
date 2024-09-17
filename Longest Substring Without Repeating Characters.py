s = "bbbb"  # Input string

maxi = 0
ns = ""

# Check if all characters in the string are the same
if len(set(s)) == 1:
    print(1)
  
else:
    # Loop to find the longest substring without repeating characters
    for i in range(len(s)):
        ns = s[i]  # Start a new substring from the current character

        for j in range(i + 1, len(s)):
            if s[j] not in ns:  # If the character is not already in the substring
                ns += s[j]
                maxi = max(len(ns), maxi)  # Update the max length
            else:
                break  # Break when a repeated character is found

    print(maxi if maxi > 0 else 1)  # Print the result

  
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
