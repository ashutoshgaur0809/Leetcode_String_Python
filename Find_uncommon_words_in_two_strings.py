s1 = "this apple is sweet"
s2 = "this apple is sour"

l1 = list(s1.split(" "))
l2 = list(s2.split(" "))
d = {}

for i in l1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in l2:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

l = []
for i,j in d.items():
    if j == 1:
        l.append(i)

print(d)
print(l)

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"

# Output: ["sweet","sour"]

# Explanation:

# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# Example 2:

# Input: s1 = "apple apple", s2 = "banana"

# Output: ["banana"]
