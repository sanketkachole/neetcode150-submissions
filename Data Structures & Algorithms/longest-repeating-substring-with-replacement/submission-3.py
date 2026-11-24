class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # # Initialize both pointers
        # left_pointer = 0
        # right_pointer = 0

        # # Initialize character frequencies
        # char_frequency = {s[0]: 1}

        # # Initialize maximum valid substring length
        # max_length = 1

        # # Expand the window
        # while right_pointer < len(s) - 1:

        #     # Move right pointer forward
        #     right_pointer += 1

        #     # Update frequency of the new character
        #     char = s[right_pointer]
        #     char_frequency[char] = char_frequency.get(char, 0) + 1

        #     # Calculate current window length
        #     substring_length = right_pointer - left_pointer + 1

        #     # Shrink window while replacements exceed k
        #     while substring_length - max(char_frequency.values()) > k:

        #         # Remove leftmost character from frequency count
        #         left_char = s[left_pointer]
        #         char_frequency[left_char] -= 1

        #         if char_frequency[left_char] == 0:
        #             del char_frequency[left_char]

        #         # Move left pointer forward
        #         left_pointer += 1

        #         # Recalculate window length
        #         substring_length = right_pointer - left_pointer + 1

        #     # Update maximum valid substring length
        #     max_length = max(max_length, substring_length)

        # return max_length

        if not s:
            return 0

        left_index = 0
        right_index = 1
        max_length = 1
        frequency = {s[0]: 1}

        while right_index < len(s):
            char = s[right_index]
            frequency[char] = frequency.get(char, 0) + 1

            max_frequency = max(frequency.values())
            window_length = right_index - left_index + 1
            replacements = window_length - max_frequency

            while replacements > k:
                frequency[s[left_index]] -= 1
                left_index += 1

                max_frequency = max(frequency.values())
                window_length = right_index - left_index + 1
                replacements = window_length - max_frequency

            max_length = max(max_length, window_length)
            right_index += 1

        return max_length




