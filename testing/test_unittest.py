import unittest
from testing import full_name

class NameTestCase(unittest.TestCase):
    """Тесты для функции full_name.py"""

    def test_first_last_name(self):
        """Имена вида 'John Doe' работвет нормально?"""
        format_name = full_name('John', 'Doe')
        self.assertEqual(format_name, 'John Doe')

    def test_first_second_last_name(self):
        """Имена вида 'John Smith Doe' работвет нормально?"""
        format_name = full_name('John', 'Smith', 'Doe')
        self.assertEqual(format_name, 'John Smith Doe')


if __name__ == "__main__":
    unittest.main()