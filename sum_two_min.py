def sum_two_min(numbers):
    """
    Возвращает сумму двух наименьших чисел в массиве.

    Args:
        numbers: Список чисел (целых или с плавающей точкой)

    Returns:
        float или int: Сумма двух наименьших чисел

    Raises:
        ValueError: Если массив содержит менее 2 элементов или нечисловые значения
    """
    if not numbers:
        raise ValueError("Массив пуст")
    if len(numbers) < 2:
        raise ValueError("Массив должен содержать как минимум два элемента")

    try:
        # Проверка, что все элементы являются числами
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("Массив содержит нечисловые значения")

        # Поиск двух наименьших чисел за один проход
        min1 = float('inf')
        min2 = float('inf')

        for num in numbers:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return min1 + min2
    except TypeError:
        raise ValueError("Массив содержит нечисловые значения")


import unittest


class TestSumTwoMin(unittest.TestCase):
    def test_normal_case(self):
        """Тест с обычным массивом чисел"""
        self.assertEqual(sum_two_min([4, 0, 3, 19, 492, -10, 1]), -10)
        self.assertEqual(sum_two_min([1, 2, 3, 4, 5]), 3)

    def test_floating_point_numbers(self):
        """Тест с числами с плавающей точкой"""
        self.assertAlmostEqual(sum_two_min([1.5, 2.5, 0.5, -0.5]), 0.0)

    def test_negative_numbers(self):
        """Тест с отрицательными числами"""
        self.assertEqual(sum_two_min([-1, -2, -3, -4]), -5)

    def test_two_elements(self):
        """Тест с ровно двумя элементами"""
        self.assertEqual(sum_two_min([5, 3]), 8)

    def test_empty_array(self):
        """Тест с пустым массивом"""
        with self.assertRaises(ValueError) as cm:
            sum_two_min([])
        self.assertEqual(str(cm.exception), "Массив пуст")

    def test_single_element(self):
        """Тест с одним элементом"""
        with self.assertRaises(ValueError) as cm:
            sum_two_min([1])
        self.assertEqual(str(cm.exception), "Массив должен содержать как минимум два элемента")

    def test_non_numeric_elements(self):
        """Тест с нечисловыми элементами"""
        with self.assertRaises(ValueError) as cm:
            sum_two_min([1, 2, "3", 4])
        self.assertEqual(str(cm.exception), "Массив содержит нечисловые значения")

    def test_duplicate_minimums(self):
        """Тест с повторяющимися минимальными значениями"""
        self.assertEqual(sum_two_min([1, 1, 2, 2]), 2)

    def test_large_numbers(self):
        """Тест с очень большими числами"""
        self.assertEqual(sum_two_min([10 ** 9, 10 ** 8, 10 ** 7, 10 ** 6]), 10 ** 6 + 10 ** 7)

    def test_large_array(self):
        """Тест с большим массивом"""
        large_array = list(range(1000000))
        self.assertEqual(sum_two_min(large_array), 0 + 1)


if __name__ == '__main__':
    unittest.main()
