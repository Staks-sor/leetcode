class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                if pairs[stack.pop()] != char:
                    return False
        
        return len(stack) == 0
