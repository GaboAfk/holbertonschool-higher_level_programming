#!/usr/bin/python3
class CountedIterator():
    def __init__(self, object):
        self.iterobject = iter(object)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            item = next(self.iterobject)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
