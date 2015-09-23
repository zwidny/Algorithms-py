from zy_sort import quick_sort, ListStack
import unittest


class TestSort(unittest.TestCase):

    def test_liststack(self):
        s = ListStack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(3, s.pop())
        self.assertEqual(2, len(s))
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(True, s.is_empty())

    def test_quick_sort(self):
        s = [24]
        self.assertEqual(s, quick_sort(s))
        s = [63, 24]
        self.assertEqual([24, 63], quick_sort(s))
        s = [80, 24, 63]
        self.assertEqual([24, 63, 80], quick_sort(s))
