#!/usr/bin/env python3
""" Module for testing client """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''
    class for tesing GithubOrgClient.org method
    '''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """
        The function `test_org` tests the `org` method of the
        `GithubOrgClient` class by asserting that the `mock_get_json`
        function is called once.
        """
        n = GithubOrgClient(f"https://api.github.com/orgs/{org}")
        n.org()
        n.org()
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """
        The function tests the public_repos_url property
        of the GithubOrgClient class.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            new = GithubOrgClient("test")
            payload = {'repos_url': 'all_repos'}
            mock_org.return_value = payload
            self.assertEqual(new._public_repos_url, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """
        The function `test_public_repos` is a unit test that checks
        if the `mock_get` function is called correctly and if the
        `mock_url` property is accessed correctly.
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            payload = {'repos_url': ["repo1", "repo2", "repo3"]}
            mock_get.return_value = payload
            mock_get()
            mock_url.return_value = mock_get
            mock_url()
            mock_url.assert_called_once()
            mock_get.assert_called_once()
