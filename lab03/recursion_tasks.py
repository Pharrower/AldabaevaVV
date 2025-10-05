"""Модуль с практическими задачами на рекурсию."""

import os
from typing import List, Optional


def binary_search_recursive(arr: List[int], target: int, 
                          left: int = 0, right: int = None) -> Optional[int]:
    """
    Рекурсивный бинарный поиск элемента в отсортированном массиве.
    
    Args:
        arr: Отсортированный массив целых чисел
        target: Искомый элемент
        left: Левая граница поиска
        right: Правая граница поиска
        
    Returns:
        Индекс элемента или None, если не найден
        
    Time Complexity: O(log n)
    Space Complexity: O(log n) - глубина рекурсии
    """
    if right is None:  # O(1)
        right = len(arr) - 1  # O(1)
    
    # Базовый случай - элемент не найден
    if left > right:  # O(1)
        return None  # O(1)
    
    mid = (left + right) // 2  # O(1)
    
    # Базовый случай - элемент найден
    if arr[mid] == target:  # O(1)
        return mid  # O(1)
    
    # Рекурсивный шаг - поиск в левой половине
    if arr[mid] > target:  # O(1)
        return binary_search_recursive(arr, target, left, mid - 1)  # T(n/2)
    
    # Рекурсивный шаг - поиск в правой половине
    return binary_search_recursive(arr, target, mid + 1, right)  # T(n/2)


def traverse_filesystem(path: str, level: int = 0) -> None:
    """
    Рекурсивный обход файловой системы с выводом дерева каталогов.
    
    Args:
        path: Путь для начала обхода
        level: Уровень вложенности (для отступов)
        
    Time Complexity: O(n) где n - количество файлов и папок
    Space Complexity: O(d) где d - глубина вложенности
    """
    try:
        # Базовый случай - путь не существует
        if not os.path.exists(path):  # O(1)
            print(" " * level + "🚫 Путь не существует")
            return
        
        # Получаем список элементов в директории
        items = os.listdir(path)  # O(k) где k - количество элементов в директории
        
        for item in items:  # O(k)
            item_path = os.path.join(path, item)  # O(1)
            
            if os.path.isdir(item_path):  # O(1)
                # Рекурсивный обход для директории
                print(" " * level + f"📁 {item}/")  # O(1)
                traverse_filesystem(item_path, level + 1)  # T(поддерево)
            else:
                # Базовый случай - файл
                print(" " * level + f"📄 {item}")  # O(1)
                
    except PermissionError:
        print(" " * level + "🚫 Нет доступа")


def hanoi_towers(n: int, source: str = "A", 
                auxiliary: str = "B", target: str = "C") -> None:
    """
    Решение задачи Ханойских башен для n дисков.
    
    Args:
        n: Количество дисков
        source: Исходный стержень
        auxiliary: Вспомогательный стержень
        target: Целевой стержень
        
    Time Complexity: O(2^n)
    Space Complexity: O(n) - глубина рекурсии
    """
    # Базовый случай - один диск
    if n == 1:  # O(1)
        print(f"Переместить диск 1 с {source} на {target}")  # O(1)
        return
    
    # Рекурсивный шаг 1: переместить n-1 дисков на вспомогательный стержень
    hanoi_towers(n - 1, source, target, auxiliary)  # T(n-1)
    
    # Переместить самый большой диск на целевой стержень
    print(f"Переместить диск {n} с {source} на {target}")  # O(1)
    
    # Рекурсивный шаг 2: переместить n-1 дисков с вспомогательного на целевой
    hanoi_towers(n - 1, auxiliary, source, target)  # T(n-1)