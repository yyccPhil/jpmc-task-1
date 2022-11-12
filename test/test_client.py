import unittest
from client import client
from random import random


class TestClient(unittest.TestCase):
    def test_getRatio1(self):
        price_a = 10
        price_b = 5
        price_ratio = client.getRatio(price_a, price_b)
        self.assertEqual(price_ratio, 2)

    def test_getRatio2(self):
        price_a = round(10 * random())
        price_b = round(10 * random())
        price_ratio = client.getRatio(price_a, price_b)
        self.assertEqual(price_ratio, price_a / price_b)

    def test_getRatio3(self):
        price_a = 10
        price_b = 0
        price_ratio = client.getRatio(price_a, price_b)
        self.assertEqual(price_ratio, None)

        # with self.assertRaises(ZeroDivisionError):
        #     price_ratio = client.getRatio(10, 0)
