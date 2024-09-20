s = "aaa"


# first gebnerate number of possible strings as per the generated stiing len is greater than 1 becoxz all 1 char string are by default palindromuic
possible_list = []
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if len(s[i:j]) > 1: 
            possible_list.append(s[i:j])

# Remove Duplicate chars with set
# possible_list = (possible_list)

# Check if string is palindromic or not
ans_list = []
for i in possible_list:
    if i == i[::-1]:
        ans_list.append(i)

        
        
print("Possible string that len is greater than 1 :",possible_list)
print("Possible String that is also plaindromica among possible_list :",ans_list)
print("So Total Palindromic Chars and Strings are :",len(s) + len(ans_list))

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
