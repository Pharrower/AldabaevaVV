"""Модуль для анализа сложности алгоритма суммирования."""

import timeit
import random
from typing import List, Optional, Callable
import matplotlib.pyplot as plt


def calculate_sum() -> None:
    """Считает сумму двух введенных чисел.
    
    Общая сложность функции: O(1)
    """
    a = int(input())  # O(1) - чтение одной строки и преобразование
    b = int(input())  # O(1)
    result = a + b  # O(1) - арифметическая операция
    print(f'Сумма чисел: {result}')  # O(1) - вывод одной строки


def sum_array(arr: List[int]) -> int:
    """Возвращает сумму всех элементов массива.
    
    Сложность: O(N), где N - длина массива.
    
    Args:
        arr: Список целых чисел для суммирования
        
    Returns:
        Сумма всех элементов массива
    """
    total = 0  # O(1) - инициализация переменной
    for num in arr:  # O(N) - цикл по всем элементам массива
        total += num  # O(1) - операция сложения и присваивания
    return total  # O(1) - возврат результата


def measure_time(func: Callable, data: List[int], number: int = 10) -> float:
    """Измеряет время выполнения функции2 в миллисекундах.
    
    Args:
        func: Функция для измерения времени выполнения
        data: Данные для передачи в функцию
        number: Количество запусков для усреднения
        
    Returns:
        Среднее время выполнения в миллисекундах
    """
    total_time = timeit.timeit(lambda: func(data), number=number)
    execution_time = total_time * 1000 / number
    return execution_time


def read_from_file(filename: str = 'input.txt') -> Optional[List[int]]:
    """Читает числа из файла и выводит содержимое.
    
    Args:
        filename: Имя файла для чтения
        
    Returns:
        Список чисел из файла или None если файл не найден
    """
    try:
        with open(filename, 'r') as file:  # O(1) - открытие файла
            content = file.read().split()  # O(N) - чтение и разделение
            numbers = [int(x) for x in content]  # O(N) - преобразование 
            
            print(f'Содержимое файла {filename}:')  # O(1)
            print(' '.join(content))  # O(N) - вывод содержимого
            
            return numbers
    except FileNotFoundError:
        print(f'Файл {filename} не найден')  # O(1)
        return None
    except ValueError:
        print('Ошибка: файл содержит нечисловые данные')  # O(1)
        return None


def main() -> None:
    """Основная функция для выполнения всех задач лабораторной работы."""
    # Характеристики ПК для тестирования
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i7-6500U @ 2.50GHz
    - Оперативная память: 8 GB
    - ОС: Windows 10 PRO
    - Python: 3.12.8
    """
    print(pc_info)
    
    # Задание 1: Сумма двух чисел из консоли
    print('=== Задание 1: Сумма двух чисел ===')
    print('Введите два целых числа:')
    calculate_sum()
    print()
    
    # Задание 2: Чтение из файла и суммирование
    print('=== Задание 2: Чтение из файла ===')
    numbers = read_from_file()
    
    if numbers:
        if len(numbers) >= 2:
            result = numbers[0] + numbers[1]  # O(1)
            print(f'Сумма первых двух чисел: {result}')  # O(1)
        else:
            print('В файле недостаточно чисел для суммирования')  # O(1)
    print()
    
    # Задание 3: Анализ производительности
    print('=== Задание 3: Анализ производительности ===')
    
    sizes = [1000, 5000, 10000, 50000, 100000, 500000]  # Размеры массивов
    times = []  # Время выполнения для каждого размера
    
    print('Замеры времени выполнения для алгоритма суммирования массива:')
    print('{:>10} {:>15} {:>20}'.format('Размер', 'Время', 'Время/элемент'))
    
    for size in sizes:
        # Генерация случайного массива заданного размера
        data = [random.randint(1, 1000) for _ in range(size)]  # O(N)
        
        # Замер времени выполнения с усреднением
        execution_time = measure_time(sum_array, data, number=10)  # O(N)
        times.append(execution_time)
        
        # Расчет времени на элемент
        time_per_element = (execution_time * 1000) / size if size > 0 else 0
        
        print('{:>10} {:>15.4f} {:>20.4f}'.format(
            size, execution_time, time_per_element
        ))
    
    # Построение графика
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, times, 'bo-', label='Измеренное время')
    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время выполнения (мс)')
    plt.title('Зависимость времени выполнения от размера\nСложность: O(N)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.savefig('time_complexity_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Анализ результатов
    print('\n=== Анализ результатов ===')
    print('1. Теоретическая сложность алгоритма: O(N)')
    print('2. Практические замеры показывают линейную зависимость T от N')
    
    # Расчет среднего времени на элемент
    avg = sum((t * 1000) / s for t, s in zip(times, sizes)) / len(sizes)
    print(f'3. Среднее время на один элемент: {avg:.4f} мкс')
    
    # Проверка на больших объемах данных
    print('4. Программа корректно обрабатывает большие объемы данных:')
    print('   - Максимальный тестируемый размер: 500,000 элементов')
    print('   - Время выполнения: {:.2f} мс'.format(times[-1]))
    print('   - Потребление памяти: линейное O(N)')


if __name__ == '__main__':
    main()