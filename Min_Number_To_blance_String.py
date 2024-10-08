class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_imbalance = 0
        
        # Traverse the string
        for char in s:
            if char == '[':
                balance += 1  # Opening bracket, increase balance
            else:
                balance -= 1  # Closing bracket, decrease balance
            
            # Track the maximum imbalance (i.e., the maximum negative balance)
            if balance < 0:
                max_imbalance = max(max_imbalance, -balance)
        
        # The number of swaps needed is half of the max imbalance
        # because each swap fixes two imbalances (one opening, one closing).
        return (max_imbalance + 1) // 2


# Example 1:

# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".
# Example 2:

# Input: s = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".
# Example 3:

# Input: s = "[]"
# Output: 0
# Explanation: The string is already balanced.
