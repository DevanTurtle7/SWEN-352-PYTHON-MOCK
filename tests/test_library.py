# Joe Wesnofske
import unittest
from unittest.mock import Mock
from library import library
import json

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = library.Library()
        # self.books_data = [{'title': 'Learning Python', 'ebook_count': 3}, {'title': 'Learning Python (Learning)', 'ebook_count': 1}, {'title': 'Learning Python', 'ebook_count': 1}, {'title': 'Learn to Program Using Python', 'ebook_count': 1}, {'title': 'Aprendendo Python', 'ebook_count': 1}, {'title': 'Python Basics', 'ebook_count': 1}]
        with open('tests_data/ebooks.txt', 'r') as f:
            self.books_data = json.loads(f.read())

lib = library

def test_setup():
    lib = library
    pass

def test_is_ebook_false():
    result = lib.is_ebook()

def test_is_ebook_true():
    return True

def test_end():
    pass
