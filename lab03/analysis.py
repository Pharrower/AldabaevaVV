"""Модуль для анализа производительности рекурсивных алгоритмов."""

import time
import timeit
import matplotlib.pyplot as plt
from recursion import factorial, fibonacci_naive, fast_power
from memoization import fibonacci_optimized
from recursion_tasks import binary_search_recursive, hanoi_towers, traverse_filesystem


def measure_time(func, *args, number: int = 1) -> float:
    """
    Измерение времени выполнения функции.
    
    Args:
        func: Функция для измерения
        *args: Аргументы функции
        number: Количество запусков для усреднения
        
    Returns:
        Среднее время выполнения в миллисекундах
    """
    def wrapper():
        return func(*args)
    
    execution_time = timeit.timeit(wrapper, number=number)  # O(number)
    return (execution_time / number) * 1000  # Конвертация в миллисекунды


def compare_fibonacci_performance() -> None:
    """Сравнение производительности наивного и мемоизированного Фибоначчи."""
    print("Сравнение производительности алгоритмов Фибоначчи:")
    print("n\tНаивный (мс)\tМемоизированный (мс)")
    print("-" * 50)
    
    n_values = list(range(10, 36, 5))  # O(1)
    naive_times = []  # O(1)
    memo_times = []  # O(1)
    
    for n in n_values:  # O(k) где k - количество значений n
        # Измеряем время для наивной версии (один запуск из-за медленности)
        naive_time = measure_time(fibonacci_naive, n, number=1)  # O(2^n)
        naive_times.append(naive_time)  # O(1)
        
        # Измеряем время для мемоизированной версии (много запусков для точности)
        memo_time = measure_time(fibonacci_optimized, n, number=100)  # O(n)
        memo_times.append(memo_time)  # O(1)
        
        print(f"{n}\t{naive_time:.2f}\t\t{memo_time:.6f}")  # O(1)
    
    # Построение графика
    plt.figure(figsize=(10, 6))  # O(1)
    plt.plot(n_values, naive_times, 'ro-', label='Наивная рекурсия', linewidth=2)  # O(k)
    plt.plot(n_values, memo_times, 'bo-', label='С мемоизацией', linewidth=2)  # O(k)
    plt.xlabel('n (номер числа Фибоначчи)')  # O(1)
    plt.ylabel('Время выполнения (мс)')  # O(1)
    plt.title('Сравнение производительности алгоритмов Фибоначчи')  # O(1)
    plt.legend()  # O(1)
    plt.grid(True, linestyle='--', alpha=0.7)  # O(1)
    plt.yscale('log')  # Логарифмическая шкала для наглядности
    plt.savefig('fibonacci_comparison.png', dpi=300, bbox_inches='tight')  # O(1)
    plt.show()  # O(1)


def test_max_recursion_depth() -> None:
    """Тестирование максимальной глубины рекурсии для обхода файловой системы."""
    print("\nТестирование обхода файловой системы:")
    
    # Создаем тестовую структуру каталогов
    test_dir = "test_directory"  # O(1)
    os.makedirs(test_dir, exist_ok=True)  # O(1)
    
    # Создаем вложенные директории
    current_path = test_dir  # O(1)
    depth = 0  # O(1)
    max_test_depth = 10  # O(1)
    
    for i in range(max_test_depth):  # O(max_test_depth)
        current_path = os.path.join(current_path, f"level_{i}")  # O(1)
        os.makedirs(current_path, exist_ok=True)  # O(1)
        depth += 1  # O(1)
        
        # Создаем тестовый файл в каждой директории
        with open(os.path.join(current_path, f"file_{i}.txt"), 'w') as f:  # O(1)
            f.write(f"Это файл на уровне {i}")  # O(1)
    
    print(f"Создана тестовая структура глубиной {depth} уровней")  # O(1)
    
    # Замеряем время обхода
    start_time = time.time()  # O(1)
    traverse_filesystem(test_dir)  # O(n)
    end_time = time.time()  # O(1)
    
    print(f"Время обхода: {(end_time - start_time) * 1000:.2f} мс")  # O(1)
    
    # Очистка тестовых файлов
    import shutil  # O(1)
    shutil.rmtree(test_dir)  # O(n)


def demonstrate_algorithms() -> None:
    """Демонстрация работы всех алгоритмов."""
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РЕКУРСИВНЫХ АЛГОРИТМОВ")
    print("=" * 60)
    
    # Факториал
    print("\n1. Вычисление факториала:")
    for i in range(6):  # O(6)
        print(f"factorial({i}) = {factorial(i)}")  # O(i)
    
    # Быстрое возведение в степень
    print("\n2. Быстрое возведение в степень:")
    base, power = 2, 10  # O(1)
    result = fast_power(base, power)  # O(log n)
    print(f"fast_power({base}, {power}) = {result}")  # O(1)
    
    # Бинарный поиск
    print("\n3. Рекурсивный бинарный поиск:")
    arr = [1, 3, 5, 7, 9, 11, 13, 15]  # O(1)
    target = 7  # O(1)
    index = binary_search_recursive(arr, target)  # O(log n)
    print(f"Массив: {arr}")  # O(n)
    print(f"Индекс элемента {target}: {index}")  # O(1)
    
    # Ханойские башни
    print("\n4. Задача Ханойских башен для 3 дисков:")
    hanoi_towers(3)  # O(2^n)


if __name__ == "__main__":
    # Характеристики ПК
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i7-1075GH @ 2.60GHz
    - Оперативная память: 16 GB DDR4
    - OC: Windows 11
    - Python: 3.9.7
    """
    print(pc_info)
    
    # Демонстрация алгоритмов
    demonstrate_algorithms()
    
    # Сравнение производительности
    compare_fibonacci_performance()
    
    # Тестирование глубины рекурсии
    test_max_recursion_depth()