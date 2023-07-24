class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        result = 0
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10
        if negative:
            result = -result
        if result < -2**31 or result > (2**31) - 1:
            return 0
        return result
