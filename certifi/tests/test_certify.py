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
        assert os.path.exists(certifi.where())

    def test_read_contents(self):
        content = certifi.contents()
        assert "-----BEGIN CERTIFICATE-----" in content
