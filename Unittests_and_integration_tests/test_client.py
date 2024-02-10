#!/usr/bin/env python3
""" Test for client.py """

import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch
import requests
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """ Test org """
        mock.return_value = {"org": org_name}
        org = GithubOrgClient("test")
        self.assertEqual(org.org, mock.return_value)
        mock.assert_called_once()

    @patch("client.GithubOrgClient.org",
           {"repos_url": "https://api.github.com/orgs/izzy"})
    def test_public_repos_url(self):
        """ Test public repos url """
        org = GithubOrgClient("izzy")
        self.assertEqual(
            org._public_repos_url,
            "https://api.github.com/orgs/izzy")

    @patch("client.get_json")
    def test_public_repos(self, mock):
        """ test public repos """
        mock.return_value = [{"name": "testing"}, {"name": "todo-app"}]
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          return_value="https://api.github.com/orgs/izzy"):
            org = GithubOrgClient("izzy")
            self.assertEqual(org.public_repos(), ["testing", "todo-app"])
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, has):
        """ Test license """
        has_license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(has_license, has)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test integration """

    @classmethod
    def setUpClass(cls):
        """ Setup class """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        cls.get_patcher = patch('client.get_json')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [org, repos]

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        cls.get_patcher.stop()

    # def test_public_repos(self):
    #     """ Test public repos """
    #     org = GithubOrgClient("test")
    #     repos = org.public_repos()
    #     payload = self.repos_payload
    #     self.assertEqual(repos, self.expected_repos)
    #     self.assertEqual(payload, self.repos_payload)


if __name__ == '__main__':
    unittest.main()
