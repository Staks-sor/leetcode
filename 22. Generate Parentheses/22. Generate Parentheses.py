class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left_count, right_count, current_str):
            if left_count > n or right_count > left_count:
                return
            if left_count == n and right_count == n:
                result.append(current_str)
                return
            dfs(left_count + 1, right_count, current_str + '(')
            dfs(left_count, right_count + 1, current_str + ')')

        result = []
        dfs(0, 0, '')
        return result
