"""Модуль с мемоизированными версиями рекурсивных алгоритмов."""

from typing import Dict


def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """
    Вычисление n-го числа Фибоначчи с мемоизацией.
    
    Args:
        n: Порядковый номер числа Фибоначчи
        memo: Словарь для кэширования результатов
        
    Returns:
        n-е число Фибоначчи
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if memo is None:  # O(1)
        memo = {}  # O(1)
    
    # Базовые случаи
    if n == 0:  # O(1)
        return 0  # O(1)
    if n == 1:  # O(1)
        return 1  # O(1)
    
    # Проверяем, есть ли результат в кэше
    if n in memo:  # O(1)
        return memo[n]  # O(1)
    
    # Вычисляем и сохраняем в кэш
    result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)  # T(n-1) + T(n-2)
    memo[n] = result  # O(1)
    
    return result  # O(1)


# Обертка для удобного использования
def fibonacci_optimized(n: int) -> int:
    """
    Оптимизированная версия вычисления чисел Фибоначчи.
    
    Args:
        n: Порядковый номер числа Фибоначчи
        
    Returns:
        n-е число Фибоначчи
    """
    return fibonacci_memo(n)