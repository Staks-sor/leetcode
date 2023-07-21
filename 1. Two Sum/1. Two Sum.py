from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Создаем пустой словарь для хранения чисел и их индексов
        for i, num in enumerate(nums):  # Перебираем список с помощью функции enumerate()
            complement = target - num  # Вычисляем значение complement
            if complement in num_dict:  # Проверяем, находится ли complement уже в словаре
                return [num_dict[complement], i]  # Если нашли пару, возвращаем индексы чисел
            num_dict[num] = i  # Добавляем число и его индекс в словарь
        return []  # Если не найдено пар чисел, возвращаем пустой список


