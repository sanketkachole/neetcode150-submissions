class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # Check whether the string is empty
        # If empty, return 0 immediately
        if not s:
            return 0
            
        # Initialize left pointer at index 0
        # Initialize right pointer at index 1
        left_pointer = 0
        right_pointer = 1

        # Create a set containing the first character
        unique_char = {s[0]}
        # Initialize maximum length to 1
        max_length = 1

        # Repeat while right pointer is within the string
        while right_pointer < len(s):

            # Check whether the character at right already exists in the set
            # While that character exists in the set:
            while s[right_pointer] in unique_char:
                # Remove the character at left from the set
                unique_char.remove(s[left_pointer])
                # Move the left pointer forward by one position
                left_pointer += 1
            # Add the character at right to the set
            unique_char.add(s[right_pointer])
            # Calculate the current window length
            # If current length exceeds maximum length:
            if len(unique_char) > max_length:
                # Update maximum length
                max_length = len(unique_char)
            # Move right pointer forward by one position
            right_pointer += 1
        # Return maximum length
        return max_length



