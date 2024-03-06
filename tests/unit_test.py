#!/usr/bin/env python3

import unittest

import sys
sys.path.append('src')

from app import Calculator

class TestAverage(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_multiply(self):
        multiply_result = self.calculator.multiply(1, 2)
        self.assertEqual(multiply_result, 2)

if __name__ == '__main__':
    unittest.main()
