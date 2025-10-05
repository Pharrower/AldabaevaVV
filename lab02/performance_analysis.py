"""Анализ производительности структур данных."""
import timeit
import matplotlib.pyplot as plt
from collections import deque
from linked_list import LinkedList


def measure_list_insert_start() -> list[float]:
    """
    Замер времени вставки в начало списка.
    
    Сложность: O(n) для list, O(1) для LinkedList
    """
    sizes = [100, 500, 1000, 2000, 5000]  # O(1)
    list_times = []  # O(1)
    linked_list_times = []  # O(1)

    for size in sizes:  # O(k) итераций
        # Тестирование list
        def list_insert() -> None:
            lst = []  # O(1)
            for i in range(size):  # O(n) итераций
                lst.insert(0, i)  # O(n) для каждой операции

        list_time = timeit.timeit(list_insert, number=10)  # O(n^2)
        list_times.append(list_time)  # O(1)

        # Тестирование LinkedList
        def linked_list_insert() -> None:
            ll = LinkedList()  # O(1)
            for i in range(size):  # O(n) итераций
                ll.insert_at_start(i)  # O(1) для каждой операции

        linked_list_time = timeit.timeit(linked_list_insert, number=10)  # O(n)
        linked_list_times.append(linked_list_time)  # O(1)

    return list_times, linked_list_times, sizes  # O(1)


def measure_queue_performance() -> list[float]:
    """
    Замер времени операций очереди.
    
    Сложность: O(n) для list.pop(0), O(1) для deque.popleft()
    """
    sizes = [1000, 5000, 10000, 50000, 100000]  # O(1)
    list_times = []  # O(1)
    deque_times = []  # O(1)

    for size in sizes:  # O(k) итераций
        # Тестирование list
        def list_queue() -> None:
            lst = list(range(size))  # O(n)
            for _ in range(size):  # O(n) итераций
                lst.pop(0)  # O(n) для каждой операции

        list_time = timeit.timeit(list_queue, number=1)  # O(n^2)
        list_times.append(list_time)  # O(1)

        # Тестирование deque
        def deque_queue() -> None:
            dq = deque(range(size))  # O(n)
            for _ in range(size):  # O(n) итераций
                dq.popleft()  # O(1) для каждой операции

        deque_time = timeit.timeit(deque_queue, number=1)  # O(n)
        deque_times.append(deque_time)  # O(1)

    return list_times, deque_times, sizes  # O(1)


def plot_results() -> None:
    """Построение графиков результатов."""
    # График для вставки в начало
    list_times_insert, linked_list_times_insert, sizes_insert = (
        measure_list_insert_start()
    )
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes_insert, list_times_insert, 'ro-', label='list.insert(0, item)')
    plt.plot(
        sizes_insert, linked_list_times_insert, 'bo-', 
        label='LinkedList.insert_at_start()'
    )
    plt.xlabel('Количество элементов')  # O(1)
    plt.ylabel('Время выполнения (сек)')  # O(1)
    plt.title('Вставка в начало\nlist O(n²) vs LinkedList O(n)')  # O(1)
    plt.legend()  # O(1)
    plt.grid(True)  # O(1)

    # График для операций очереди
    list_times_queue, deque_times_queue, sizes_queue = (
        measure_queue_performance()
    )
    
    plt.subplot(1, 2, 2)
    plt.plot(sizes_queue, list_times_queue, 'ro-', label='list.pop(0)')
    plt.plot(sizes_queue, deque_times_queue, 'go-', label='deque.popleft()')
    plt.xlabel('Количество элементов')  # O(1)
    plt.ylabel('Время выполнения (сек)')  # O(1)
    plt.title('Удаление из начала\nlist O(n²) vs deque O(n)')  # O(1)
    plt.legend()  # O(1)
    plt.grid(True)  # O(1)

    plt.tight_layout()  # O(1)
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')  # O(1)
    plt.show()  # O(1)


def print_pc_info() -> None:
    """Вывод информации о системе."""
    pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i7-6500U @ 2.50GHz
- Оперативная память: 8 GB
- ОС: Windows 10 PRO
- Python: 3.12.8
"""
    print(pc_info)


if __name__ == '__main__':
    print_pc_info()
    plot_results()