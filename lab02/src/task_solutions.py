from collections import deque

def check_brackets_balance(expression):
    """
    Проверка сбалансированности скобок с использованием стека.
    
    Args:
        expression: Строка со скобками
        
    Returns:
        True если скобки сбалансированы, иначе False
        
    Complexity: O(n)
    """
    stack = []  # O(1) - создание стека
    brackets = {')': '(', ']': '[', '}': '{'}  # O(1) - создание словаря
    
    for char in expression:  # O(n) - цикл по символам
        if char in '([{':  # O(1) - проверка
            stack.append(char)  # O(1) - добавление в стек
        elif char in brackets:  # O(1) - проверка
            if not stack or stack[-1] != brackets[char]:  # O(1) - проверка
                return False  # O(1) - возврат
            stack.pop()  # O(1) - удаление из стека
    
    return len(stack) == 0  # O(1) - проверка и возврат


def is_palindrome_deque(text):
    """
    Проверка строки на палиндром с использованием дека.
    
    Args:
        text: Строка для проверки
        
    Returns:
        True если строка - палиндром, иначе False
        
    Complexity: O(n)
    """
    # Очистка строки от пробелов и приведение к нижнему регистру
    cleaned = ''.join(char.lower() for char in text if char.isalnum())  # O(n)
    
    dq = deque(cleaned)  # O(n) - создание дека
    
    while len(dq) > 1:  # O(n) - цикл
        if dq.popleft() != dq.pop():  # O(1) - сравнение
            return False  # O(1) - возврат
    
    return True  # O(1) - возврат


class PrintQueue:
    """Очередь печати на основе deque."""
    
    def __init__(self):
        """Инициализация очереди."""  # O(1) - инициализация
        self.queue = deque()  # O(1) - создание дека
    
    def enqueue(self, task):
        """
        Добавление задачи в очередь.
        
        Args:
            task: Задача для печати
            
        Complexity: O(1)
        """
        self.queue.append(task)  # O(1) - добавление в конец
    
    def dequeue(self):
        """
        Извлечение задачи из очереди.
        
        Returns:
            Задача или None если очередь пуста
            
        Complexity: O(1)
        """
        if self.queue:  # O(1) - проверка
            return self.queue.popleft()  # O(1) - удаление из начала
        return None  # O(1) - возврат
    
    def process_queue(self):
        """
        Обработка всех задач в очереди.
        
        Complexity: O(n)
        """
        print('Обработка очереди печати:')
        while self.queue:  # O(n) - цикл
            task = self.dequeue()  # O(1) - извлечение
            print(f'Печатается: {task}')  # O(1) - вывод
        print('Все задачи обработаны.')  # O(1) - вывод
    
    def is_empty(self):
        """
        Проверка пустоты очереди.
        
        Returns:
            True если очередь пуста, иначе False
            
        Complexity: O(1)
        """
        return len(self.queue) == 0  # O(1) - проверка


def test_practical_tasks():
    """Тестирование практических задач."""
    # Тест проверки скобок
    test_expressions = [
        '()',
        '()[]{}',
        '([{}])',
        '(]',
        '([)]',
        '((()'
    ]
    
    print('Проверка сбалансированности скобок:')
    for expr in test_expressions:
        result = check_brackets_balance(expr)
        print(f'"{expr}" -> {"Сбалансированы" if result else "Не сбалансированы"}')
    
    print('\n' + '='*50 + '\n')
    
    # Тест проверки палиндромов
    test_strings = [
        'А роза упала на лапу Азора',
        'racecar',
        'hello',
        'Madam, I\'m Adam',
        'not a palindrome'
    ]
    
    print('Проверка палиндромов:')
    for text in test_strings:
        result = is_palindrome_deque(text)
        print(f'"{text}" -> {"Палиндром" if result else "Не палиндром"}')
    
    print('\n' + '='*50 + '\n')
    
    # Тест очереди печати
    print('Симуляция очереди печати:')
    print_queue = PrintQueue()
    
    # Добавляем задачи в очередь
    tasks = ['Документ1.pdf', 'Отчет.docx', 'Презентация.pptx', 'Изображение.jpg']
    for task in tasks:
        print_queue.enqueue(task)
        print(f'Добавлено в очередь: {task}')
    
    print()
    print_queue.process_queue()


if __name__ == '__main__':
    test_practical_tasks()