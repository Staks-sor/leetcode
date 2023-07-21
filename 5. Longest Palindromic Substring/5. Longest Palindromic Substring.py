class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""

        for i in range(len(s)):
            # Checking odd length palindromes
            palindrome = self.expand_from_middle(s, i, i)
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome
            
            # Checking even length palindromes
            palindrome = self.expand_from_middle(s, i, i+1)
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome

        return max_palindrome
    
    def expand_from_middle(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]
