"""
Модуль для визуализации результатов тестирования.
"""

import matplotlib.pyplot as plt
import numpy as np
from performance_test import run_performance_tests


def plot_time_vs_size(results: dict, data_type: str = 'random'):
    """
    Построение графика зависимости времени от размера массива.

    Args:
        results: Результаты тестирования
        data_type: Тип данных для построения графика
    """
    plt.figure(figsize=(12, 8))

    algorithms = list(results.keys())
    sizes = sorted(list(next(iter(results.values()))[data_type].keys()))

    for algo_name in algorithms:
        times = []
        for size in sizes:
            time_val = results[algo_name][data_type][size]['time']
            times.append(time_val)

        plt.plot(sizes, times, marker='o', label=algo_name, linewidth=2)

    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (секунды)')
    plt.title(f'Зависимость времени сортировки от размера массива ({data_type} данные)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig(f'time_vs_size_{data_type}.png', dpi=300, bbox_inches='tight')
    plt.show()


def plot_time_vs_datatype(results: dict, size: int = 5000):
    """
    Построение графика зависимости времени от типа данных.

    Args:
        results: Результаты тестирования
        size: Фиксированный размер массива
    """
    plt.figure(figsize=(12, 8))

    algorithms = list(results.keys())
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']

    x = np.arange(len(data_types))
    width = 0.15

    for i, algo_name in enumerate(algorithms):
        times = []
        for data_type in data_types:
            if size in results[algo_name][data_type]:
                time_val = results[algo_name][data_type][size]['time']
                times.append(time_val)
            else:
                times.append(0)

        plt.bar(x + i * width - width * (len(algorithms) - 1) / 2, 
                times, width, label=algo_name)

    plt.xlabel('Тип данных')
    plt.ylabel('Время выполнения (секунды)')
    plt.title(f'Сравнение времени сортировки для разных типов данных (размер {size})')
    plt.xticks(x, data_types)
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(f'time_vs_datatype_size_{size}.png',
                dpi=300, bbox_inches='tight')
    plt.show()


def create_summary_table(results: dict):
    """Создание сводной таблицы результатов."""
    print("\n" + "="*80)
    print("СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ")
    print("="*80)

    sizes = sorted(list(next(iter(results.values()))['random'].keys()))
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']

    for data_type in data_types:
        print(f"\n{data_type.upper()} ДАННЫЕ:")
        print("-" * 60)
        header = f"{'Алгоритм':<15} " + "".join([f"{size:>12}" for size in sizes])
        print(header)
        print("-" * 60)

        for algo_name in results.keys():
            row = f"{algo_name:<15}"
            for size in sizes:
                if size in results[algo_name][data_type]:
                    time_val = results[algo_name][data_type][size]['time']
                    row += f"{time_val:>12.6f}"
                else:
                    row += f"{'N/A':>12}"
            print(row)


if __name__ == "__main__":
    # Запуск тестов и построение графиков
    print("Running performance tests for visualization...")
    results = run_performance_tests(sizes=[100, 1000, 5000, 10000], num_runs=1)

    # Построение графиков
    plot_time_vs_size(results, 'random')
    plot_time_vs_datatype(results, 5000)

    # Создание сводной таблицы
    create_summary_table(results)