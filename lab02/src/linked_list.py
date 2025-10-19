class Node:
    """Узел связного списка."""
    
    def __init__(self, data):
        """
        Инициализация узла.
        
        Args:
            data: Данные для хранения в узле
        """
        self.data = data  # O(1) - присваивание
        self.next = None  # O(1) - присваивание


class LinkedList:
    """Односвязный список."""
    
    def __init__(self):
        """Инициализация пустого списка."""  # O(1) - инициализация
        self.head = None  # O(1) - присваивание
        self.tail = None  # O(1) - присваивание
        self.size = 0     # O(1) - присваивание
    
    def insert_at_start(self, data):
        """
        Вставка элемента в начало списка.
        
        Args:
            data: Данные для вставки
            
        Complexity: O(1)
        """
        new_node = Node(data)  # O(1) - создание узла
        
        if self.head is None:  # O(1) - проверка
            self.head = new_node  # O(1) - присваивание
            self.tail = new_node  # O(1) - присваивание
        else:
            new_node.next = self.head  # O(1) - присваивание
            self.head = new_node       # O(1) - присваивание
        
        self.size += 1  # O(1) - инкремент
    
    def insert_at_end(self, data):
        """
        Вставка элемента в конец списка.
        
        Args:
            data: Данные для вставки
            
        Complexity: O(1) - с использованием tail
        """
        new_node = Node(data)  # O(1) - создание узла
        
        if self.head is None:  # O(1) - проверка
            self.head = new_node  # O(1) - присваивание
            self.tail = new_node  # O(1) - присваивание
        else:
            self.tail.next = new_node  # O(1) - присваивание
            self.tail = new_node       # O(1) - присваивание
        
        self.size += 1  # O(1) - инкремент
    
    def delete_from_start(self):
        """
        Удаление элемента из начала списка.
        
        Returns:
            Удаленные данные или None если список пуст
            
        Complexity: O(1)
        """
        if self.head is None:  # O(1) - проверка
            return None
        
        data = self.head.data  # O(1) - доступ
        
        if self.head == self.tail:  # O(1) - проверка
            self.head = None  # O(1) - присваивание
            self.tail = None  # O(1) - присваивание
        else:
            self.head = self.head.next  # O(1) - присваивание
        
        self.size -= 1  # O(1) - декремент
        return data     # O(1) - возврат
    
    def traversal(self):
        """
        Обход всех элементов списка.
        
        Returns:
            Список всех элементов
            
        Complexity: O(n)
        """
        elements = []           # O(1) - создание списка
        current = self.head     # O(1) - присваивание
        
        while current:          # O(n) - цикл по всем элементам
            elements.append(current.data)  # O(1) - добавление в список
            current = current.next         # O(1) - переход к следующему
        
        return elements  # O(1) - возврат
    
    def is_empty(self):
        """
        Проверка пустоты списка.
        
        Returns:
            True если список пуст, иначе False
            
        Complexity: O(1)
        """
        return self.head is None  # O(1) - проверка


# Общая сложность класса: зависит от вызываемых методов