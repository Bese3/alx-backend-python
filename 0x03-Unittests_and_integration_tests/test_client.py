#!/usr/bin/env python3
""" Module for testing client """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, licence_key, expected):
        """
        The function `test_has_licence` tests the `has_license`
        method of the `GithubOrgClient` class by asserting that
        the result matches the expected value.
        """
        Obj = GithubOrgClient("test")
        self.assertEqual(Obj.has_license(repo, licence_key), expected)


@parameterized_class(
    (
                      "org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"
    ),
    TEST_PAYLOAD
                      )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""
        my_config = {'return_value.json.side_effect':
                     [
                         cls.org_payload, cls.repos_payload,
                         cls.expected_repos, cls.apache2_repos
                     ]
                     }
        cls.get_patcher = patch('requests.get', **my_config)
        cls.mock = cls.get_patcher.start()
        cls.test = GithubOrgClient('google')

    def test_public_repos(self):
        """ Integration test: public repos"""
        self.assertEqual(self.test.org, self.org_payload)
        self.assertEqual(self.test.repos_payload, self.repos_payload)
        self.assertEqual(self.test.public_repos(), self.expected_repos)
        self.assertEqual(self.test.public_repos('FAKE_LISENCE'), [])
        self.mock.assert_called()

    def test_public_repos_with_lisence(self):
        """ Integration test for public repos with License """
        self.assertEqual(self.test.public_repos(), self.expected_repos)
        self.assertEqual(self.test.public_repos('FAKE_LISENCE'), [])
        self.assertEqual(self.test.public_repos("apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()
        del cls.test
