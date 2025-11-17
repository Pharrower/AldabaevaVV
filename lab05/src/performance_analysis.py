"""Анализ производительности хеш-таблиц."""

import time
import random
import string
import matplotlib.pyplot as plt
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


def generate_random_string(length: int = 10) -> str:
    """Генерация случайной строки."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def measure_performance():
    """Измерение производительности разных реализаций."""
    # Параметры тестирования
    table_sizes = [100, 500, 1000]
    load_factors = [0.1, 0.5, 0.7, 0.9]
    hash_functions = ['simple', 'polynomial', 'djb2']
    
    results = {}
    
    for size in table_sizes:
        for load_factor in load_factors:
            num_elements = int(size * load_factor)
            
            # Генерация тестовых данных
            test_data = []
            for _ in range(num_elements):
                key = generate_random_string()
                value = generate_random_string()
                test_data.append((key, value))
            
            # Тестирование разных реализаций
            implementations = [
                ('Chaining', HashTableChaining(size=size)),
                ('Linear Probing', HashTableOpenAddressing(size=size, probing_method='linear')),
                ('Double Hashing', HashTableOpenAddressing(size=size, probing_method='double'))
            ]
            
            for impl_name, ht in implementations:
                # Измерение времени вставки
                start_time = time.time()
                for key, value in test_data:
                    ht.insert(key, value)
                insert_time = time.time() - start_time
                
                # Измерение времени поиска
                start_time = time.time()
                for key, value in test_data:
                    ht.search(key)
                search_time = time.time() - start_time
                
                # Статистика коллизий
                if hasattr(ht, 'get_collision_stats'):
                    collisions, _ = ht.get_collision_stats()
                else:
                    collisions = 0
                
                key = (size, load_factor, impl_name)
                results[key] = {
                    'insert_time': insert_time,
                    'search_time': search_time,
                    'collisions': collisions,
                    'load_factor': ht.load_factor
                }
                
                print(f"Size: {size}, Load: {load_factor}, Impl: {impl_name}")
                print(f"  Insert: {insert_time:.6f}s, Search: {search_time:.6f}s")
                print(f"  Collisions: {collisions}")
    
    return results


def plot_results(results):
    """Построение графиков результатов."""
    # Группировка результатов по реализации
    implementations = ['Chaining', 'Linear Probing', 'Double Hashing']
    load_factors = [0.1, 0.5, 0.7, 0.9]
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Производительность хеш-таблиц')
    
    # Время вставки
    ax = axes[0, 0]
    for impl in implementations:
        times = []
        for lf in load_factors:
            key = (100, lf, impl)  # Для размера 100
            times.append(results[key]['insert_time'])
        ax.plot(load_factors, times, marker='o', label=impl)
    ax.set_title('Время вставки (размер=100)')
    ax.set_xlabel('Коэффициент заполнения')
    ax.set_ylabel('Время (сек)')
    ax.legend()
    ax.grid(True)
    
    # Время поиска
    ax = axes[0, 1]
    for impl in implementations:
        times = []
        for lf in load_factors:
            key = (100, lf, impl)
            times.append(results[key]['search_time'])
        ax.plot(load_factors, times, marker='o', label=impl)
    ax.set_title('Время поиска (размер=100)')
    ax.set_xlabel('Коэффициент заполнения')
    ax.set_ylabel('Время (сек)')
    ax.legend()
    ax.grid(True)
    
    # Коллизии
    ax = axes[1, 0]
    for impl in implementations:
        collisions = []
        for lf in load_factors:
            key = (100, lf, impl)
            collisions.append(results[key]['collisions'])
        ax.plot(load_factors, collisions, marker='o', label=impl)
    ax.set_title('Количество коллизий (размер=100)')
    ax.set_xlabel('Коэффициент заполнения')
    ax.set_ylabel('Коллизии')
    ax.legend()
    ax.grid(True)
    
    # Сравнение хеш-функций
    ax = axes[1, 1]
    hash_funcs = ['simple', 'polynomial', 'djb2']
    collisions_by_func = []
    
    for hf in hash_funcs:
        ht = HashTableChaining(size=100, hash_func=hf)
        test_data = [(generate_random_string(), generate_random_string()) 
                    for _ in range(70)]  # load_factor = 0.7
        for key, value in test_data:
            ht.insert(key, value)
        coll, _ = ht.get_collision_stats()
        collisions_by_func.append(coll)
    
    ax.bar(hash_funcs, collisions_by_func)
    ax.set_title('Коллизии по хеш-функциям')
    ax.set_xlabel('Хеш-функция')
    ax.set_ylabel('Количество коллизий')
    ax.grid(True)
    
    plt.tight_layout()
    plt.savefig('performance_results.png')
    plt.show()


if __name__ == '__main__':
    print("Запуск анализа производительности...")
    results = measure_performance()
    print("\nПостроение графиков...")
    plot_results(results)
    print("Анализ завершен. Результаты сохранены в performance_results.png")