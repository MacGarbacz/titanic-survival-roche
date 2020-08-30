from src import helpers as h
import unittest
import numpy as np


class TestHelpers(unittest.TestCase):
    def test_categorize_age(self):
        valid_age = 15
        edge_age = 33
        invalid_age = 150
        none_age = np.NaN

        self.assertEqual(h.categorize_age(valid_age), 1)
        self.assertEqual(h.categorize_age(edge_age), 3)
        self.assertEqual(h.categorize_age(invalid_age), 0)
        self.assertEqual(h.categorize_age(none_age), 0)

    def test_categorize_fare(self):
        valid_fare = 8.5
        edge_fare = 7.9
        invalid_fare = 2000
        none_fare = np.NaN

        self.assertEqual(h.categorize_fare(valid_fare), 2)
        self.assertEqual(h.categorize_fare(edge_fare), 1)
        self.assertEqual(h.categorize_fare(invalid_fare), 5)
        self.assertEqual(h.categorize_fare(none_fare), 5)

    def test_extract_title(self):
        valid_name = "James Mr. John"
        invalid_name = "James John"

        self.assertEqual(h.extract_title(valid_name), "Mr.")
        self.assertEqual(h.extract_title(invalid_name), "")

    def test_convert_title(self):
        valid_title = "Mr."
        uncommon_title = "Rev."
        empty_title = ""

        self.assertEqual(h.convert_title(valid_title), 1)
        self.assertEqual(h.convert_title(uncommon_title), 0)
        self.assertEqual(h.convert_title(empty_title), 0)


if __name__ == '__main__':
    unittest.main()
