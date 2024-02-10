#!/usr/bin/env python3
'''
Unit testing & Integrated testing
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''
    class for testing access_nested_map method
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)

    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        The function `test_access_nested_map` is used to test the
        `access_nested_map` function by comparing its output with
        an expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", ), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        The function `test_access_nested_map_exception` tests if accessing
        a nested map with a given path raises a `KeyError` with the
        expected error message.
        """
        with self.assertRaises(KeyError) as keyerror:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(keyerror.exception), F"KeyError('{expected}')")


class TestGetJson(unittest.TestCase):
    '''
    class for testing get_json method
    '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_request_get):
        """
        The function `test_get_json` tests the `get_json`
        function by mocking a request and response and asserting
        that the returned JSON matches the expected value.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_payload
        mock_request_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''
    class for testing memoize method
    '''
    def test_memoize(self):
        """
        The function `test_memoize` tests the functionality of the
        `memoize` decorator on a property of a class.
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test1 = TestClass()
            test1.a_property()
            test1.a_property()
            mock.assert_called_once()
