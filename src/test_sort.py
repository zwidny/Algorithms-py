import unittest

from zy_sort import quick_sort, merge


class TestSort(unittest.TestCase):

    def test_quick_sort(self):
        s = [24]
        self.assertEqual(s, quick_sort(s))
        s = [63, 24]
        self.assertEqual([24, 63], quick_sort(s))
        s = [80, 24, 63]
        self.assertEqual([24, 63, 80], quick_sort(s))

    def test_merge(self):
        s = [24]
        self.assertEqual(s, merge(s))
        s = [63, 24]
        self.assertEqual([24, 63], merge(s))
        s = [80, 24, 63]
        self.assertEqual([24, 63, 80], merge(s))
