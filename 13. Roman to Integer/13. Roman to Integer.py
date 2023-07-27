class Solution:
    def romanToInt(self, s: str) -> int:
        roman_vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            if i < n - 1 and roman_vals[s[i]] < roman_vals[s[i+1]]:
                total -= roman_vals[s[i]]
            else:
                total += roman_vals[s[i]]
        
        return total
