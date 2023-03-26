import unittest
from library import patron
from unittest.mock import Mock, call

"""
Add_borrowed_book
Get_borrowed_books
Return_boorrowed_book
__eq__
__ne__
"""

class TestPatron(unittest.TestCase):

    def setUp(self):
        self.pat = patron.Patron('fname', 'lname', '20', '1234')

    def test_valid_name(self):
        pat = patron.Patron('fname', 'lname', '20', '1234')
        self.assertTrue(isinstance(pat, patron.Patron))

    def test_invalid_name(self):
        self.assertRaises(patron.InvalidNameException, patron.Patron, '1fname', '1lname', '20', '1234')
    
    def test_add_borrowed_book(self):
        self.pat.borrowed_books = [] 
        self.pat.add_borrowed_book('test')
        self.assertEqual(self.pat.borrowed_books, ['test'])
    
    def test_add_borrowed_book_exists(self):
        self.pat.borrowed_books = ['book']
        self.pat.add_borrowed_book('book')
        self.assertEqual(self.pat.borrowed_books, ['book'])
    
    def test_get_borrowed_books(self):
        borrowed_books_mock = Mock()
        self.pat.borrowed_books = borrowed_books_mock
        self.assertEqual(self.pat.get_borrowed_books(), borrowed_books_mock)
    
    def test_return_borrowed_book_not_taken(self):
        borrowed_books = ['book1', 'book3']
        self.pat.borrowed_books = borrowed_books
        self.pat.return_borrowed_book('book2')
        self.assertEqual(self.pat.borrowed_books, borrowed_books)
    
    def test_return_borrowed_book(self):
        borrowed_books = ['book1', 'book2', 'book3']
        self.pat.borrowed_books = borrowed_books
        self.pat.return_borrowed_book('book1')
        self.assertEqual(self.pat.borrowed_books, ['book2', 'book3'])
    
    def test_equals(self):
        dict = {}
        other = Mock()
        other.__dict__ = dict 
        self.pat.__dict__ = dict 
        self.assertTrue(self.pat == other)

    def test_not_equals(self):
        not_equals_mock = Mock()
        self.pat.__eq__ = not_equals_mock
        self.pat.__ne__(Mock())
        self.pat.__eq__.assert_called_once()
    
    def test_get_fname(self):
        self.assertEqual(self.pat.get_fname(), 'fname');

    def test_get_lname(self):
        self.assertEqual(self.pat.get_lname(),'lname');

    def test_get_age(self):
        self.assertEqual(self.pat.get_age(), '20');

    def test_get_memberID(self):
        self.assertEqual(self.pat.get_memberID(), '1234');

    def test_new_patron_numbers_fname(self):
      self.assertRaises(patron.InvalidNameException, patron.Patron, '1fname', 'name', '20', '1234')

    def test_new_patron_numbers_lname(self):
      self.assertRaises(patron.InvalidNameException, patron.Patron, 'fname', '1name', '20', '1234')
    
    def test_name_with_numbers_raises_message(self):
        self.assertRaisesRegex(patron.InvalidNameException, "^Name should not contain numbers$", patron.Patron, '1fname', 'lname', '20', '1234')