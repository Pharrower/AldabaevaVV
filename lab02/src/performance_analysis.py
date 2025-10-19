import timeit
import matplotlib.pyplot as plt
from collections import deque
from linked_list import LinkedList


def measure_list_insert_start(n):
    """
    Измерение времени вставки в начало списка.
    
    Args:
        n: Количество элементов для вставки
        
    Returns:
        Время выполнения в миллисекундах
    """
    def operation():
        lst = []  # O(1) - создание списка
        for i in range(n):  # O(n) - цикл
            lst.insert(0, i)  # O(n) - вставка в начало
    
    time_taken = timeit.timeit(operation, number=1)  # O(n^2) - общая сложность
    return time_taken * 1000  # O(1) - умножение


def measure_linked_list_insert_start(n):
    """
    Измерение времени вставки в начало связного списка.
    
    Args:
        n: Количество элементов для вставки
        
    Returns:
        Время выполнения в миллисекундах
    """
    def operation():
        ll = LinkedList()  # O(1) - создание списка
        for i in range(n):  # O(n) - цикл
            ll.insert_at_start(i)  # O(1) - вставка в начало
    
    time_taken = timeit.timeit(operation, number=1)  # O(n) - общая сложность
    return time_taken * 1000  # O(1) - умножение


def measure_list_dequeue(n):
    """
    Измерение времени удаления из начала списка.
    
    Args:
        n: Количество операций удаления
        
    Returns:
        Время выполнения в миллисекундах
    """
    def operation():
        lst = list(range(n))  # O(n) - создание списка
        for _ in range(n):  # O(n) - цикл
            if lst:  # O(1) - проверка
                lst.pop(0)  # O(n) - удаление из начала
    
    time_taken = timeit.timeit(operation, number=1)  # O(n^2) - общая сложность
    return time_taken * 1000  # O(1) - умножение


def measure_deque_dequeue(n):
    """
    Измерение времени удаления из начала дека.
    
    Args:
        n: Количество операций удаления
        
    Returns:
        Время выполнения в миллисекундах
    """
    def operation():
        dq = deque(range(n))  # O(n) - создание дека
        for _ in range(n):  # O(n) - цикл
            if dq:  # O(1) - проверка
                dq.popleft()  # O(1) - удаление из начала
    
    time_taken = timeit.timeit(operation, number=1)  # O(n) - общая сложность
    return time_taken * 1000  # O(1) - умножение


def run_performance_analysis():
    """Запуск анализа производительности."""
    # Характеристики ПК для тестирования
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i7-6500U @ 2.50GHz
    - Оперативная память: 8 GB
    - OC: Windows 10 PRO
    - Python: 3.12.8
    """
    print(pc_info)
    
    # Тестируемые размеры
    sizes = [100, 500, 1000, 2000, 5000]
    
    # Результаты измерений
    list_insert_times = []
    linked_list_insert_times = []
    list_dequeue_times = []
    deque_dequeue_times = []
    
    print('Сравнение вставки в начало:')
    print('Размер | List (мс) | LinkedList (мс)')
    print('-' * 40)
    
    for size in sizes:
        list_time = measure_list_insert_start(size)
        linked_list_time = measure_linked_list_insert_start(size)
        
        list_insert_times.append(list_time)
        linked_list_insert_times.append(linked_list_time)
        
        print(f'{size:6} | {list_time:9.2f} | {linked_list_time:14.2f}')
    
    print('\nСравнение удаления из начала (очередь):')
    print('Размер | List (мс) | Deque (мс)')
    print('-' * 40)
    
    for size in sizes:
        list_time = measure_list_dequeue(size)
        deque_time = measure_deque_dequeue(size)
        
        list_dequeue_times.append(list_time)
        deque_dequeue_times.append(deque_time)
        
        print(f'{size:6} | {list_time:9.2f} | {deque_time:10.2f}')
    
    # Построение графиков
    plt.figure(figsize=(12, 5))
    
    # График 1: Сравнение вставки в начало
    plt.subplot(1, 2, 1)
    plt.plot(sizes, list_insert_times, 'ro-', label='List insert(0)')
    plt.plot(sizes, linked_list_insert_times, 'bo-', label='LinkedList insert_at_start')
    plt.xlabel('Количество элементов')
    plt.ylabel('Время (мс)')
    plt.title('Вставка в начало\nList: O(n²) vs LinkedList: O(n)')
    plt.legend()
    plt.grid(True)
    
    # График 2: Сравнение удаления из начала
    plt.subplot(1, 2, 2)
    plt.plot(sizes, list_dequeue_times, 'ro-', label='List pop(0)')
    plt.plot(sizes, deque_dequeue_times, 'go-', label='Deque popleft()')
    plt.xlabel('Количество элементов')
    plt.ylabel('Время (мс)')
    plt.title('Удаление из начала\nList: O(n²) vs Deque: O(n)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return {
        'sizes': sizes,
        'list_insert': list_insert_times,
        'linked_list_insert': linked_list_insert_times,
        'list_dequeue': list_dequeue_times,
        'deque_dequeue': deque_dequeue_times
    }


if __name__ == '__main__':
    results = run_performance_analysis()