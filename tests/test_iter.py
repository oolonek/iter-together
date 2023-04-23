# -*- coding: utf-8 -*-

"""Tests for ``iter-together``."""

import unittest
from iter_together_pma import utils
from tests.constants import F1_PATH, F2_PATH

class TestIterTogether(unittest.TestCase):
    """Tests for iter_together package."""
    
    def setUp(self) -> None:
        self.constant1 = 5
    
    def test_iter_together(self):
        """Test that two files can iterate together."""
        expected = [
            ('a', 'a_1', 'a_2'),
            ('b', 'b_1', 'b_2'),
            ('c', 'c_1', 'c_2'),
            ('d', 'd_1', 'd_2'),
        ]
        result = list(utils.iter_together(F1_PATH, F2_PATH))
        self.assertIsNotNone(result)
        self.assertLess(0, len(result))
        self.assertEqual(expected, result)
        
    def test_failure_on_bad_keys(self):
        """_summary_"""