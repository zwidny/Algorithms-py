# -*- coding: utf-8 -*-


class ListStack:
    """LIFO Stack implementation using list
    """

    def __init__(self):
        self.data_repo = []

    def __len__(self):
        return len(self.data_repo)

    def is_empty(self):
        return len(self.data_repo) == 0

    def push(self, element):
        self.data_repo.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data_repo.pop()
