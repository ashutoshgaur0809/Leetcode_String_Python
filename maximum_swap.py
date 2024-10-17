class Solution:
    def maximumSwap(self, num: int) -> int:

        a = []
        s = str(num)
        for i in s:
            a.append(int(i))

    

        for i in range(len(a)):
            print(a[i:])
            if a[i] != max(a[i:]):
            
                max_index = a.index(max(a[i:]))
            
                a[i], a[max_index] = a[max_index], a[i]
                break

        s = ""
        for i in a:
            s += str(i)
        
        return int(s)

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
