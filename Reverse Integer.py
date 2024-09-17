class Solution:
    def reverse(self, x: int) -> int:

        s = str(x)
    
        if s[0] == "-":
            # Handle negative numbers: reverse the part after the minus sign
            reversed_s = "-" + s[:0:-1]
        else:
            # Handle positive numbers: reverse the entire string
            reversed_s = s[::-1]

        # Convert back to integer
        result = int(reversed_s)
        
        # Ensure the result is within the 32-bit signed integer range
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
