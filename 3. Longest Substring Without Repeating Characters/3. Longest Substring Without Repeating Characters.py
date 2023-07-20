class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = right = 0
        max_length = 0
        unique_chars = set()

        while right < n:
            if s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            else:
                unique_chars.add(s[right])
                right += 1
                max_length = max(max_length, right - left)

        return max_length
