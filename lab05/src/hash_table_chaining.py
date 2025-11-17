"""Реализация хеш-таблицы с методом цепочек."""

from typing import Any, Optional, Tuple
from hash_functions import simple_hash, polynomial_hash, djb2_hash


class HashTableChaining:
    """Хеш-таблица с методом цепочек для разрешения коллизий."""

    def __init__(self, size: int = 101, hash_func: str = 'simple', 
                 load_factor_threshold: float = 0.7):
        """
        Инициализация хеш-таблицы.

        Args:
            size: Начальный размер таблицы (простое число)
            hash_func: Используемая хеш-функция ('simple', 'polynomial', 'djb2')
            load_factor_threshold: Порог коэффициента заполнения для рехеширования
        """
        self.size = size
        self.count = 0
        self.load_factor_threshold = load_factor_threshold
        self.table = [[] for _ in range(size)]

        # Выбор хеш-функции
        hash_functions = {
            'simple': simple_hash,
            'polynomial': polynomial_hash,
            'djb2': djb2_hash
        }
        self.hash_func = hash_functions[hash_func]

    def _hash(self, key: str) -> int:
        """Вычисление хеша для ключа."""
        return self.hash_func(key, self.size)

    def _resize(self, new_size: int) -> None:
        """Изменение размера таблицы и перехеширование всех элементов."""
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key: str, value: Any) -> None:
        """
        Вставка элемента в хеш-таблицу.

        Args:
            key: Ключ
            value: Значение

        Time Complexity: O(1) в среднем, O(n) в худшем случае
        """
        # Проверка необходимости рехеширования
        if self.load_factor > self.load_factor_threshold:
            self._resize(self.size * 2)

        index = self._hash(key)
        bucket = self.table[index]

        # Проверка на существование ключа
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Вставка нового элемента
        bucket.append((key, value))
        self.count += 1

    def search(self, key: str) -> Optional[Any]:
        """
        Поиск элемента по ключу.

        Args:
            key: Ключ для поиска

        Returns:
            Найденное значение или None

        Time Complexity: O(1) в среднем, O(n) в худшем случае
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key: str) -> bool:
        """
        Удаление элемента по ключу.

        Args:
            key: Ключ для удаления

        Returns:
            True если элемент удален, False если не найден

        Time Complexity: O(1) в среднем, O(n) в худшем случае
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    @property
    def load_factor(self) -> float:
        """Коэффициент заполнения таблицы."""
        return self.count / self.size

    def get_collision_stats(self) -> Tuple[int, float]:
        """
        Статистика коллизий.

        Returns:
            (количество коллизий, средняя длина цепочки)
        """
        collisions = 0
        total_chain_length = 0

        for bucket in self.table:
            if len(bucket) > 1:
                collisions += len(bucket) - 1
            total_chain_length += len(bucket)

        avg_chain_length = total_chain_length / self.size if self.size > 0 else 0
        return collisions, avg_chain_length