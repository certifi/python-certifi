# -*- coding: utf-8 -*-
"""
unit tests to make sure everything behaves as expected
"""

import os
import unittest

import certifi


class TestCertifi(unittest.TestCase):
    def test_cabundle_exists(self):
        """Check that the reported bundle exists"""
        self.assertTrue(os.path.exists(certifi.where()))

    def test_read_contents(self):
        """Check that the returned contents contain a certificate"""
        self.assertIn("-----BEGIN CERTIFICATE-----", certifi.contents())
