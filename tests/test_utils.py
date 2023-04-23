import unittest
import iter_together

from tests.constants import F1_PATH, F2_PATH

class TestIterTogether(unittest.TestCase):
    """Tests for iter_together package."""
    
    def test_iter_together(self):
        """Test that two files can iterate together."""
        expected = [
            ('a', 'a_1', 'a_2'),
            ('b', 'b_1', 'b_2'),
            ('c', 'c_1', 'c_2'),
            ('d', 'd_1', 'd_2'),
        ]
        result = list(iter_together.iter_together(F1_PATH, F2_PATH))
        self.assertIsNotNone(result)
        self.assertLess(0, len(result))
        self.assertEqual(expected, result)
        