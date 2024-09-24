class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_prefix_length = 0  # Variable to store the maximum length of the common prefix
        
        # Iterate through each element in arr1
        for num1 in arr1:
            str_num1 = str(num1)  # Convert the first number to a string
            
            # Iterate through each element in arr2
            for num2 in arr2:
                str_num2 = str(num2)  # Convert the second number to a string
                
                # Find the common prefix length between the two strings
                current_prefix_length = 0
                for k in range(min(len(str_num1), len(str_num2))):
                    if str_num1[k] == str_num2[k]:
                        current_prefix_length += 1
                    else:
                        break  # Stop when a mismatch is found
                
                # Update the maximum prefix length found so far
                max_prefix_length = max(max_prefix_length, current_prefix_length)
        
        return max_prefix_length
      
# Example 1:

# Input: arr1 = [1,10,100], arr2 = [1000]
# Output: 3
# Explanation: There are 3 pairs (arr1[i], arr2[j]):
# - The longest common prefix of (1, 1000) is 1.
# - The longest common prefix of (10, 1000) is 10.
# - The longest common prefix of (100, 1000) is 100.
# The longest common prefix is 100 with a length of 3.
# Example 2:

# Input: arr1 = [1,2,3], arr2 = [4,4,4]
# Output: 0
# Explanation: There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
# Note that common prefixes between elements of the same array do not count.

# arr1 = [10]
# arr2 = [17, 11]
# output-> 1
