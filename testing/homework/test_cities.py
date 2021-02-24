import unittest
from city_functions import geo

tour = geo('chile', 'santiago')

class NameTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        format_geo = geo('chile', 'santiago')
        self.assertEqual(format_geo, 'Santiago, Chile')


print(tour)


if __name__ == "__main__":
    unittest.main()