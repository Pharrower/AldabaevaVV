"""Реализация связного списка."""
from typing import Any, Optional


class Node:
    """Узел связного списка."""

    def __init__(self, data: Any) -> None:
        """
        Инициализация узла.
        
        Сложность: O(1)
        """
        self.data = data  # O(1)
        self.next: Optional['Node'] = None  # O(1)


class LinkedList:
    """Односвязный список."""

    def __init__(self) -> None:
        """
        Инициализация пустого списка.
        
        Сложность: O(1)
        """
        self.head: Optional[Node] = None  # O(1)
        self.tail: Optional[Node] = None  # O(1)
        self.length = 0  # O(1)

    def is_empty(self) -> bool:
        """
        Проверка на пустоту списка.
        
        Сложность: O(1)
        """
        return self.head is None  # O(1)

    def insert_at_start(self, data: Any) -> None:
        """
        Вставка элемента в начало списка.
        
        Сложность: O(1)
        """
        new_node = Node(data)  # O(1)
        if self.is_empty():  # O(1)
            self.head = new_node  # O(1)
            self.tail = new_node  # O(1)
        else:
            new_node.next = self.head  # O(1)
            self.head = new_node  # O(1)
        self.length += 1  # O(1)

    def insert_at_end(self, data: Any) -> None:
        """
        Вставка элемента в конец списка.
        
        Сложность: O(1) - благодаря хвостовому указателю
        """
        new_node = Node(data)  # O(1)
        if self.is_empty():  # O(1)
            self.head = new_node  # O(1)
            self.tail = new_node  # O(1)
        else:
            self.tail.next = new_node  # O(1)
            self.tail = new_node  # O(1)
        self.length += 1  # O(1)

    def delete_from_start(self) -> Any:
        """
        Удаление элемента из начала списка.
        
        Сложность: O(1)
        """
        if self.is_empty():  # O(1)
            raise IndexError('Список пуст')  # O(1)

        data = self.head.data  # O(1)
        self.head = self.head.next  # O(1)
        
        if self.head is None:  # O(1)
            self.tail = None  # O(1)
            
        self.length -= 1  # O(1)
        return data  # O(1)

    def traversal(self) -> list[Any]:
        """
        Обход списка и возврат элементов.
        
        Сложность: O(n)
        """
        elements = []  # O(1)
        current = self.head  # O(1)
        while current is not None:  # O(n) итераций
            elements.append(current.data)  # O(1)
            current = current.next  # O(1)
        return elements  # O(1)

    def search(self, target: Any) -> bool:
        """
        Поиск элемента в списке.
        
        Сложность: O(n)
        """
        current = self.head  # O(1)
        while current is not None:  # O(n) итераций
            if current.data == target:  # O(1)
                return True  # O(1)
            current = current.next  # O(1)
        return False  # O(1)

    def __len__(self) -> int:
        """
        Возвращает длину списка.
        
        Сложность: O(1)
        """
        return self.length  # O(1)

    def __str__(self) -> str:
        """
        Строковое представление списка.
        
        Сложность: O(n)
        """
        elements = self.traversal()  # O(n)
        return ' -> '.join(map(str, elements))  # O(n)