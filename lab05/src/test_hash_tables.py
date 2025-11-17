"""Unit-тесты для хеш-таблиц."""

import unittest
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


class TestHashTables(unittest.TestCase):
    """Тесты для всех реализаций хеш-таблиц."""

    def test_chaining_basic_operations(self):
        """Тест базовых операций для метода цепочек."""
        ht = HashTableChaining(size=10)

        # Тест вставки и поиска
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        self.assertEqual(ht.search("key1"), "value1")
        self.assertEqual(ht.search("key2"), "value2")
        self.assertIsNone(ht.search("key3"))

        # Тест обновления
        ht.insert("key1", "new_value1")
        self.assertEqual(ht.search("key1"), "new_value1")

        # Тест удаления
        self.assertTrue(ht.delete("key1"))
        self.assertIsNone(ht.search("key1"))
        self.assertFalse(ht.delete("key1"))

    def test_open_addressing_linear_basic_operations(self):
        """Тест базовых операций для открытой адресации с линейным пробированием."""
        ht = HashTableOpenAddressing(size=10, probing_method='linear')

        # Тест вставки и поиска
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        self.assertEqual(ht.search("key1"), "value1")
        self.assertEqual(ht.search("key2"), "value2")
        self.assertIsNone(ht.search("key3"))

        # Тест обновления
        ht.insert("key1", "new_value1")
        self.assertEqual(ht.search("key1"), "new_value1")

        # Тест удаления
        self.assertTrue(ht.delete("key1"))
        self.assertIsNone(ht.search("key1"))
        self.assertFalse(ht.delete("key1"))

    def test_open_addressing_double_basic_operations(self):
        """Тест базовых операций для открытой адресации с двойным хешированием."""
        ht = HashTableOpenAddressing(size=10, probing_method='double')

        # Тест вставки и поиска
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        self.assertEqual(ht.search("key1"), "value1")
        self.assertEqual(ht.search("key2"), "value2")

        # Тест удаления
        self.assertTrue(ht.delete("key1"))
        self.assertIsNone(ht.search("key1"))

    def test_collision_handling(self):
        """Тест обработки коллизий."""
        # Используем маленькую таблицу для гарантии коллизий
        ht_chaining = HashTableChaining(size=3)
        ht_linear = HashTableOpenAddressing(size=3, probing_method='linear')
        ht_double = HashTableOpenAddressing(size=3, probing_method='double')

        keys = ["a", "b", "c", "d"]  # Должны быть коллизии

        for ht in [ht_chaining, ht_linear, ht_double]:
            for i, key in enumerate(keys):
                ht.insert(key, f"value{i}")

            # Проверяем, что все значения доступны
            for i, key in enumerate(keys):
                self.assertEqual(ht.search(key), f"value{i}")

    def test_resize_operation(self):
        """Тест операции изменения размера."""
        ht = HashTableChaining(size=5, load_factor_threshold=0.6)

        # Вставляем элементы для触发 рехеширования
        for i in range(10):
            ht.insert(f"key{i}", f"value{i}")

        # Проверяем, что все значения доступны после рехеширования
        for i in range(10):
            self.assertEqual(ht.search(f"key{i}"), f"value{i}")


if __name__ == '__main__':
    unittest.main()