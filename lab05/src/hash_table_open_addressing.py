"""Реализация хеш-таблицы с открытой адресацией."""

from typing import Any, Optional, Tuple
from hash_functions import simple_hash, polynomial_hash, djb2_hash


class HashItem:
    """Элемент хеш-таблицы для открытой адресации."""

    def __init__(self, key: Optional[str] = None, value: Any = None):
        self.key = key
        self.value = value
        self.is_deleted = False


class HashTableOpenAddressing:
    """Хеш-таблица с открытой адресацией."""

    def __init__(self, size: int = 101, hash_func: str = 'simple',
                 probing_method: str = 'linear', load_factor_threshold: float = 0.7):
        """
        Инициализация хеш-таблицы.

        Args:
            size: Начальный размер таблицы (простое число)
            hash_func: Используемая хеш-функция
            probing_method: Метод пробирования ('linear', 'double')
            load_factor_threshold: Порог коэффициента заполнения
        """
        self.size = size
        self.count = 0
        self.deleted_count = 0
        self.load_factor_threshold = load_factor_threshold
        self.probing_method = probing_method
        self.table = [HashItem() for _ in range(size)]

        # Выбор хеш-функции
        hash_functions = {
            'simple': simple_hash,
            'polynomial': polynomial_hash,
            'djb2': djb2_hash
        }
        self.hash_func = hash_functions[hash_func]

    def _hash(self, key: str, attempt: int = 0) -> int:
        """Вычисление хеша с учетом номера попытки."""
        if self.probing_method == 'linear':
            return (self.hash_func(key, self.size) + attempt) % self.size
        elif self.probing_method == 'double':
            h1 = self.hash_func(key, self.size)
            h2 = 1 + (self.hash_func(key, self.size - 1))
            return (h1 + attempt * h2) % self.size
        else:
            raise ValueError("Неизвестный метод пробирования")

    def _resize(self, new_size: int) -> None:
        """Изменение размера таблицы и перехеширование."""
        old_table = self.table
        self.size = new_size
        self.table = [HashItem() for _ in range(new_size)]
        self.count = 0
        self.deleted_count = 0

        for item in old_table:
            if item.key is not None and not item.is_deleted:
                self.insert(item.key, item.value)

    def insert(self, key: str, value: Any) -> None:
        """
        Вставка элемента в хеш-таблицу.

        Args:
            key: Ключ
            value: Значение

        Time Complexity: O(1) в среднем, O(n) в худшем случае
        """
        # Проверка необходимости рехеширования
        if self.effective_load_factor > self.load_factor_threshold:
            self._resize(self.size * 2)

        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            item = self.table[index]

            if item.key is None or item.is_deleted:
                # Нашли свободную ячейку
                item.key = key
                item.value = value
                item.is_deleted = False
                self.count += 1
                if item.key is None:  # Была полностью пустая ячейка
                    self.count += 0  # Уже учтено в self.count
                return
            elif item.key == key:
                # Обновление существующего ключа
                item.value = value
                item.is_deleted = False
                return

            attempt += 1

        # Если не нашли место - рехеширование
        self._resize(self.size * 2)
        self.insert(key, value)

    def search(self, key: str) -> Optional[Any]:
        """
        Поиск элемента по ключу.

        Args:
            key: Ключ для поиска

        Returns:
            Найденное значение или None

        Time Complexity: O(1) в среднем, O(n) в худшем случае
        """
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            item = self.table[index]

            if item.key is None and not item.is_deleted:
                # Достигли пустой ячейки
                return None
            elif item.key == key and not item.is_deleted:
                # Нашли ключ
                return item.value

            attempt += 1

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
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            item = self.table[index]

            if item.key is None and not item.is_deleted:
                return False
            elif item.key == key and not item.is_deleted:
                item.is_deleted = True
                self.count -= 1
                self.deleted_count += 1

                # Периодическая очистка удаленных элементов
                if self.deleted_count > self.count:
                    self._resize(self.size)

                return True

            attempt += 1

        return False

    @property
    def load_factor(self) -> float:
        """Коэффициент заполнения таблицы."""
        return (self.count + self.deleted_count) / self.size

    @property
    def effective_load_factor(self) -> float:
        """Эффективный коэффициент заполнения (без учета удаленных)."""
        return self.count / self.size

    def get_collision_stats(self) -> Tuple[int, int]:
        """
        Статистика коллизий.

        Returns:
            (количество коллизий, максимальная длина пробирования)
        """
        collisions = 0
        max_probe_length = 0

        for i, item in enumerate(self.table):
            if item.key is not None and not item.is_deleted:
                original_index = self._hash(item.key, 0)
                if original_index != i:
                    collisions += 1
                    probe_length = abs(i - original_index) % self.size
                    max_probe_length = max(max_probe_length, probe_length)

        return collisions, max_probe_length