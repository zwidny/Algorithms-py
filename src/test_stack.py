import unittest

from zy_stack import ListStack


class TestStack(unittest.TestCase):

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
