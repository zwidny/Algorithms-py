from zy_sort import quick_sort
import unittest


class TestSort(unittest.TestCase):

    def test_quick_sort(self):
        s = [24]
        self.assertEqual(s, quick_sort(s))
        s = [63, 24]
        self.assertEqual([24, 63], quick_sort(s))
        s = [80, 24, 63]
        self.assertEqual([24, 63, 80], quick_sort(s))
