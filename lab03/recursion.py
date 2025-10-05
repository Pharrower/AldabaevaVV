"""Модуль с рекурсивными алгоритмами."""


def factorial(n: int) -> int:
    """
    Вычисление факториала числа n рекурсивным методом.
    
    Args:
        n: Целое неотрицательное число
        
    Returns:
        Факториал числа n
        
    Time Complexity: O(n)
    Space Complexity: O(n) - глубина рекурсии
    """
    # Базовый случай
    if n == 0 or n == 1:  # O(1)
        return 1  # O(1)
    
    # Рекурсивный шаг
    return n * factorial(n - 1)  # O(1) + T(n-1)


def fibonacci_naive(n: int) -> int:
    """
    Наивное вычисление n-го числа Фибоначчи.
    
    Args:
        n: Порядковый номер числа Фибоначчи
        
    Returns:
        n-е число Фибоначчи
        
    Time Complexity: O(2^n) - экспоненциальная
    Space Complexity: O(n) - глубина рекурсии
    """
    # Базовые случаи
    if n == 0:  # O(1)
        return 0  # O(1)
    if n == 1:  # O(1)
        return 1  # O(1)
    
    # Рекурсивный шаг
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)  # T(n-1) + T(n-2)


def fast_power(a: float, n: int) -> float:
    """
    Быстрое возведение числа a в степень n через степень двойки.
    
    Args:
        a: Основание
        n: Показатель степени
        
    Returns:
        a в степени n
        
    Time Complexity: O(log n)
    Space Complexity: O(log n) - глубина рекурсии
    """
    # Базовый случай
    if n == 0:  # O(1)
        return 1  # O(1)
    
    # Если степень отрицательная
    if n < 0:  # O(1)
        return 1 / fast_power(a, -n)  # O(1) + T(-n)
    
    # Рекурсивный шаг для четной степени
    if n % 2 == 0:  # O(1)
        half_power = fast_power(a, n // 2)  # T(n/2)
        return half_power * half_power  # O(1)
    
    # Рекурсивный шаг для нечетной степени
    return a * fast_power(a, n - 1)  # O(1) + T(n-1)