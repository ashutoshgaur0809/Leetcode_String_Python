# Example 1:

# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

# Example 2:

# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
s = "dwmodizxvvbosxxw"
ns = set(list(s[:]))
print("Unique Chars of S->",ns)
dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]

l = ""

for i in dictionary:
    l+=i

li = set(list(l))
# print(l)
print("Unique Char in Dict ->",li)


# Create new list for those char who not in dict
nl = []

for i in ns:
    if i not in li:
        nl.append(i)
for i in li:
    if i not in ns:
        nl.append(i)
nl = set(nl)
print("list for those char who not in dict ->",nl)

# Find occurence of each char of new list in main string

clk = 0
for i in nl:
    clk += s.count(i)
    
print("Count Of unused chars from main string ->",clk)
    



    
