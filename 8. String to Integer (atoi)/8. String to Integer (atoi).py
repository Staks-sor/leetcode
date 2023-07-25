class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if s == "":
            return 0

        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1

        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1

        try:
            num = int(s[:i])
        except:
            return 0

        num *= sign
        num = max(min(num, 2**31 - 1), -2**31)

        return num
