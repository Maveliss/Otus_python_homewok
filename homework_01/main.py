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

def filter_numbers(numbers_list, filter_type):
    if filter_type == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    if filter_type == PRIME:
        prime_numbers = []
        for number in numbers_list:
            if number < 2:
                continue
            for i in range(2, number):
                if (number % i) == 0:
                        break
            else:
                prime_numbers.append(number)
        return prime_numbers


print(filter_numbers([1, 2, 3], ODD))
print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([2, 3, 4, 5, 7, 11, 15, 17, 20, 25], PRIME))
"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""
