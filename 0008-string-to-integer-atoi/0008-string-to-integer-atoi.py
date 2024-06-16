class Solution:
    def string_to_number(self, input_string: str, last: int) -> int:
        # Base Case
        if last == 0:
            return int(input_string[last])
        
        # Recursive Call
        small_ans = self.string_to_number(input_string, last - 1)
        
        # Small Work
        current_digit = int(input_string[last])
        return small_ans * 10 + current_digit

    def myAtoi(self, s: str) -> int:
        # Clean up the string
        s = s.strip()
        if not s:
            return 0

        # Determine if there is a sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Extract the numeric part of the string
        num_str = ''
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break

        if not num_str:
            return 0

        # Use the helper function to convert the string to a number
        last_index = len(num_str) - 1
        number = self.string_to_number(num_str, last_index)

        result = sign * number

        # Clamp the result to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result

