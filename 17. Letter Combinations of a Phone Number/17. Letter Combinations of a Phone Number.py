from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Маппинг цифр к буквам
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # Рекурсивная функция для поиска комбинаций
        def backtrack(combination, next_digits):
            # Базовый случай - нет следующих цифр
            if len(next_digits) == 0:
                output.append(combination)
            # Рекурсивно генерируем комбинации
            else:
                for letter in mapping[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output
