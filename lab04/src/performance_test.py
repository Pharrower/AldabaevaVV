"""
Модуль для тестирования производительности алгоритмов сортировки.
"""

import time
import copy
from typing import List, Dict, Tuple
from lab04.src.sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, is_sorted
from lab04.src.generate_data import generate_test_data


# Словарь с алгоритмами сортировки
SORTING_ALGORITHMS = {
    'bubble_sort': bubble_sort,
    'selection_sort': selection_sort,
    'insertion_sort': insertion_sort,
    'merge_sort': merge_sort,
    'quick_sort': quick_sort
}


def measure_time(sort_func, arr: List[int]) -> Tuple[float, List[int]]:
    """
    Измерение времени выполнения сортировки.

    Returns:
        Кортеж (время в секундах, отсортированный массив)
    """
    arr_copy = copy.deepcopy(arr)
    start_time = time.time()
    sorted_arr = sort_func(arr_copy)
    end_time = time.time()
    return end_time - start_time, sorted_arr


def run_performance_tests(sizes: List[int] = None, num_runs: int = 1) -> Dict:
    """
    Запуск тестов производительности для всех алгоритмов и типов данных.

    Args:
        sizes: Список размеров массивов для тестирования
        num_runs: Количество запусков для усреднения

    Returns:
        Словарь с результатами тестов
    """
    if sizes is None:
        sizes = [100, 1000, 5000, 10000]

    # Генерация тестовых данных
    test_data = generate_test_data(sizes)

    results = {}

    for algo_name, sort_func in SORTING_ALGORITHMS.items():
        results[algo_name] = {}
        print(f"Testing {algo_name}...")

        for data_type, sizes_dict in test_data.items():
            results[algo_name][data_type] = {}

            for size, original_arr in sizes_dict.items():
                total_time = 0.0
                is_correct = True

                for run in range(num_runs):
                    time_taken, sorted_arr = measure_time(sort_func, original_arr)
                    total_time += time_taken

                    # Проверка корректности сортировки
                    if run == 0 and not is_sorted(sorted_arr):
                        is_correct = False

                avg_time = total_time / num_runs
                results[algo_name][data_type][size] = {
                    'time': avg_time,
                    'correct': is_correct
                }

                status = "✓" if is_correct else "✗"
                print(f"  {data_type} (size {size}): {avg_time:.6f}s {status}")

    return results


def verify_all_sorts():
    """Проверка корректности всех алгоритмов сортировки."""
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(test_arr)

    print("Verifying sorting algorithms:")
    for algo_name, sort_func in SORTING_ALGORITHMS.items():
        result = sort_func(test_arr.copy())
        is_correct = result == expected
        status = "PASS" if is_correct else "FAIL"
        print(f"  {algo_name}: {status}")
        if not is_correct:
            print(f"    Expected: {expected}")
            print(f"    Got: {result}")


if __name__ == "__main__":
    # Проверка корректности сортировки
    verify_all_sorts()
    print()

    # Запуск тестов производительности
    print("Running performance tests...")
    results = run_performance_tests(sizes=[100, 1000, 5000], num_runs=1)