"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers, power=2):
    results = []
    for num in numbers:
        results.append(num ** power)
    return results
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

print(power_numbers(1, 2, 5, 7))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

"""
def filter_numbers():
    
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
