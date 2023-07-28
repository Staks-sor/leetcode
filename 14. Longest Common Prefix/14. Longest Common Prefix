
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_len = min(len(s) for s in strs)
        first_str = strs[0]

        for idx in range(min_len):
            char = first_str[idx]
            for s in strs[1:]:
                if s[idx] != char:
                    return first_str[:idx]
        
        return first_str[:min_len]
