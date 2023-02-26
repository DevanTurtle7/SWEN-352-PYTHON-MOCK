# Joe Wesnofske
import unittest
from unittest.mock import Mock
from library import library
from library import patron
import json

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = library.Library()
        self.books_data = [{'title': 'Learning Python', 'ebook_count': 3}, {'title': 'Learning Python (Learning)', 'ebook_count': 1}, {'title': 'Learning Python', 'ebook_count': 1}, {'title': 'Learn to Program Using Python', 'ebook_count': 1}, {'title': 'Aprendendo Python', 'ebook_count': 1}, {'title': 'Python Basics', 'ebook_count': 1}]
        # with open('tests_data/ebooks.txt', 'r') as f:
        #     self.books_data = json.loads(f.read())

    def test_is_ebook_true(self): # HINT
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertTrue(self.lib.is_ebook('learning python'))
    
    def test_is_ebook_false(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertFalse(self.lib.is_ebook('notatitle'))

    def test_get_ebooks_count(self): # HINT
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertEqual(self.lib.get_ebooks_count("learning python"), 8)

    def test_is_book_by_author_true(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertEqual(self.lib.is_book_by_author("Sarah J. Maas", "A Court of Mist and Fury"), True)

    def test_is_book_by_author_false(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertEqual(self.lib.is_book_by_author("Sarah J. Maas", "Arabian Love Poems"), False)

    def test_get_languages_for_book_english(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertEqual(self.lib.get_languages_for_book("Arabian Love Poems"), {"eng"})
    
    def test_get_languages_for_book_multiple(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertEqual(self.lib.get_languages_for_book("Cinna"), {'eng','ger','tam','spa','mal','ita','nep','tel','fre','dut'})

    def test_register_patron(self):
        self.lib.register_patron("Joe", "Wesnofske", "21", "6160")
        self.assertEqual(self.lib.db.get_all_patrons(), [{"fname": "Joe", "lname": "Wesnofske", "age": "21", "memberID": "6160", "borrowed_books": []}])

    def test_is_patron_registered_true(self):
        self.lib.register_patron("Joe", "Wesnofske", "21", "6160")
        patron = library.Patron("Joe", "Wesnofske", "21", "6160")
        self.assertEqual(self.lib.is_patron_registered(patron), True)
    
    def test_is_patron_registered_false(self):
        self.lib.register_patron("Joe", "Wesnofske", "21", "6160")
        patron = library.Patron("Joe", "Wesnofske", "21", "5555")
        self.assertEqual(self.lib.is_patron_registered(patron), False)
        
    def test_borrow_book(self):
        patron = library.Patron("Joe", "Wesnofske", "21", "6160")
        self.lib.borrow_book("Cinna", patron)
        self.assertEqual(self.lib.db.get_all_patrons(), [{"fname": "Joe", "lname": "Wesnofske", "age": "21", "memberID": "6160", "borrowed_books": ["cinna"]}])
        self.lib.return_borrowed_book("Cinna", patron)
    
    def test_return_borrowed_book(self):
        patron = library.Patron("Joe", "Wesnofske", "21", "6160")
        self.lib.borrow_book("Cinna", patron)
        self.lib.return_borrowed_book("Cinna", patron)
        self.assertEqual(self.lib.db.get_all_patrons(), [{"fname": "Joe", "lname": "Wesnofske", "age": "21", "memberID": "6160", "borrowed_books": []}])

    def test_is_book_borrowed_true(self):
        patron = library.Patron("Joe", "Wesnofske", "21", "6160")
        self.lib.borrow_book("Arabian Love Poems", patron)
        self.assertTrue(self.lib.is_book_borrowed("Arabian Love Poems", patron))
        self.lib.return_borrowed_book("Arabian Love Poems", patron)
    
    def test_is_book_borrowed_false(self):
        patron = library.Patron("Joe", "Wesnofske", "21", "6160")
        self.lib.borrow_book("Arabian Love Poems", patron)
        self.assertFalse(self.lib.is_book_borrowed("Cinna", patron))
        self.lib.return_borrowed_book("Arabian Love Poems", patron)


    def test_end(self):
        pass
