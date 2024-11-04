#!/usr/bin/env python3
""" Testing utils """
import unittest
from typing import Dict, Tuple, Any
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict[str, Any],
                                         path: Tuple[str]
                                         ) -> None:
        ''' Tests that a KeyError is raised when the path is invalid '''
        with self.assertRaises(KeyError) as error_handler:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error_handler.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    ''' test get_json '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict[str, Any],
                      mock_get: Mock
                      ) -> None:
        ''' Test get_json '''
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)

    