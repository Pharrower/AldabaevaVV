"""Решение практических задач."""
from collections import deque
from typing import Any


def check_brackets(expression: str) -> bool:
    """
    Проверка сбалансированности скобок.
    
    Сложность: O(n)
    """
    stack = []  # O(1)
    brackets = {')': '(', ']': '[', '}': '{'}  # O(1)
    
    for char in expression:  # O(n) итераций
        if char in '([{':  # O(1)
            stack.append(char)  # O(1)
        elif char in brackets:  # O(1)
            if not stack or stack[-1] != brackets[char]:  # O(1)
                return False  # O(1)
            stack.pop()  # O(1)
    
    return len(stack) == 0  # O(1)


def is_palindrome(sequence: str) -> bool:
    """
    Проверка, является ли последовательность палиндромом.
    
    Сложность: O(n)
    """
    dq = deque(sequence.lower().replace(' ', ''))  # O(n)
    
    while len(dq) > 1:  # O(n) итераций
        if dq.popleft() != dq.pop():  # O(1)
            return False  # O(1)
    
    return True  # O(1)


class PrintQueue:
    """Симуляция очереди печати."""

    def __init__(self) -> None:
        """
        Инициализация очереди печати.
        
        Сложность: O(1)
        """
        self.queue = deque()  # O(1)

    def add_task(self, task: str) -> None:
        """
        Добавление задачи в очередь.
        
        Сложность: O(1)
        """
        self.queue.append(task)  # O(1)
        print(f'Задача "{task}" добавлена в очередь печати')  # O(1)

    def process_task(self) -> Any:
        """
        Обработка следующей задачи.
        
        Сложность: O(1)
        """
        if not self.queue:  # O(1)
            print('Очередь печати пуста')  # O(1)
            return None  # O(1)
        
        task = self.queue.popleft()  # O(1)
        print(f'Печатается: {task}')  # O(1)
        return task  # O(1)

    def show_queue(self) -> None:
        """
        Показать текущую очередь.
        
        Сложность: O(n)
        """
        if not self.queue:  # O(1)
            print('Очередь пуста')  # O(1)
        else:
            print('Текущая очередь печати:', list(self.queue))  # O(n)


def test_solutions() -> None:
    """Тестирование решений."""
    # Тестирование проверки скобок
    test_expressions = [
        '((()))',
        '([{}])',
        '({[}])',
        '((())',
        ''
    ]
    
    print('Проверка сбалансированности скобок:')
    for expr in test_expressions:
        result = check_brackets(expr)
        print(f'  {expr}: {result}')
    
    # Тестирование палиндромов
    test_sequences = [
        'А роза упала на лапу Азора',
        'racecar',
        'hello',
        'a',
        ''
    ]
    
    print('\nПроверка палиндромов:')
    for seq in test_sequences:
        result = is_palindrome(seq)
        print(f'  "{seq}": {result}')
    
    # Тестирование очереди печати
    print('\nСимуляция очереди печати:')
    printer = PrintQueue()
    printer.add_task('Документ1.pdf')
    printer.add_task('Отчет.docx')
    printer.add_task('Презентация.pptx')
    
    printer.show_queue()
    printer.process_task()
    printer.process_task()
    printer.show_queue()


if __name__ == '__main__':
    test_solutions()