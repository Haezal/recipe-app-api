"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test calculation functions"""

    def test_add_numbers(self):
        """Test that values are added together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substracting numbers"""
        res = calc.substract(15, 10)
        self.assertEqual(res, 5)
