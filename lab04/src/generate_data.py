"""
Модуль для генерации тестовых данных.
"""

import random
from typing import List, Dict


def generate_random_array(size: int) -> List[int]:
    """Генерация случайного массива."""
    return [random.randint(0, 10000) for _ in range(size)]


def generate_sorted_array(size: int) -> List[int]:
    """Генерация отсортированного массива."""
    return list(range(size))


def generate_reversed_array(size: int) -> List[int]:
    """Генерация массива, отсортированного в обратном порядке."""
    return list(range(size, 0, -1))


def generate_almost_sorted_array(size: int) -> List[int]:
    """Генерация почти отсортированного массива (95% упорядочено)."""
    arr = list(range(size))
    # Перемешиваем 5% элементов
    num_shuffled = max(1, size // 20)
    for _ in range(num_shuffled):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def generate_test_data(sizes: List[int]) -> Dict[str, Dict[int, List[int]]]:
    """
    Генерация всех типов тестовых данных для заданных размеров.

    Returns:
        Словарь с данными в формате:
        {
            'random': {100: [...], 1000: [...], ...},
            'sorted': {100: [...], 1000: [...], ...},
            'reversed': {100: [...], 1000: [...], ...},
            'almost_sorted': {100: [...], 1000: [...], ...}
        }
    """
    data_types = {
        'random': generate_random_array,
        'sorted': generate_sorted_array,
        'reversed': generate_reversed_array,
        'almost_sorted': generate_almost_sorted_array
    }

    test_data = {}
    for data_type, generator in data_types.items():
        test_data[data_type] = {}
        for size in sizes:
            test_data[data_type][size] = generator(size)

    return test_data


if __name__ == "__main__":
    # Тест генерации данных
    test_sizes = [100, 500]
    data = generate_test_data(test_sizes)

    for data_type, sizes_dict in data.items():
        print(f"{data_type}:")
        for size, arr in sizes_dict.items():
            print(f"  Size {size}: first 10 elements - {arr[:10]}")
        print()