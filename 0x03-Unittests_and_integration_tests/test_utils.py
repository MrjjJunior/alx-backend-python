#!/usr/bin/env python3
""" Testing utils """
import unittest
from typing import Dict, Tuple, Any
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    ''' Test '''

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict[str, Any],
                               path: Tuple[str],
                               expected: Any
                               ) -> None:
        """ Test access nested map """

        self.assertEqual(access_nested_map(nested_map, path), expected)
