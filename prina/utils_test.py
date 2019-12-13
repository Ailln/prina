import unittest

from .utils import prina


class UtilsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_utils(self):
        a = "1"
        b = 2
        c = True
        self.assertEqual(prina("test"), "test")
        self.assertEqual(prina(a, b, c), "a: 1 b: 2 c: True")
        self.assertEqual(prina(a, b, c, "test"), "a: 1 b: 2 c: True test")


if __name__ == '__main__':
    unittest.main()
