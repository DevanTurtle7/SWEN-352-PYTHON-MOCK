import unittest
from unittest.mock import Mock, call
from library import ext_api_interface
import requests
import json

class TestExtApiInterface(unittest.TestCase):

    def setUp(self):
        self.api = ext_api_interface.Books_API()
        self.book = "learning python"
        self.book_author = 'Nick Mason'
        with open('tests_data/ebooks.txt', 'r') as f:
            self.data_get_ebooks = json.loads(f.read())
        with open('tests_data/json_data.txt', 'r') as f:
            self.json_data = json.loads(f.read())
        with open('tests_data/json_author_data.txt', 'r') as f:
            self.json_author_data = json.loads(f.read())
        with open('tests_data/availability.txt', 'r') as f:
            self.data_availability = json.loads(f.read())
        with open('tests_data/books_by_author.txt', 'r') as f:
            self.data_books_by_author = json.loads(f.read())
        with open('tests_data/get_book_info.txt', 'r') as f:
            self.data_get_book_info = json.loads(f.read())

    def test_make_request_True(self):
        attr = {'json.return_value': dict()}
        requests.get = Mock(return_value = Mock(status_code = 200, **attr))
        self.assertEqual(self.api.make_request(""), dict())

    def test_make_request_connection_error(self):
        ext_api_interface.requests.get = Mock(side_effect=requests.ConnectionError)
        url = "some url"
        self.assertEqual(self.api.make_request(url), None)

    def test_make_request_False(self):
        requests.get = Mock(return_value=Mock(status_code=100))
        self.assertEqual(self.api.make_request(""), None)
    
    def test_is_book_available(self):
      self.api.make_request = Mock(return_value=self.json_data)
      self.assertEqual(self.api.is_book_available(self.book), self.data_availability)

    def test_is_book_available_zero(self):
      multi_book_data = {'docs':[]};
      self.api.make_request = Mock(return_value=multi_book_data)
      self.assertEqual(self.api.is_book_available(self.book), False)

    def test_is_book_available_one(self):
      multi_book_data = {'docs':[True]};
      self.api.make_request = Mock(return_value=multi_book_data)
      self.assertEqual(self.api.is_book_available(self.book), True)

    def test_is_book_available_multiple(self):
      multi_book_data = {'docs':[True, True, True]};
      self.api.make_request = Mock(return_value=multi_book_data)
      self.assertEqual(self.api.is_book_available(self.book), True)

    def test_is_book_available_true(self):
      def check_input(url):
       if url == "http://openlibrary.org/search.json?q="+self.book:
           return self.json_data
       else:
           None
      self.api.make_request = Mock(side_effect=check_input)
      self.assertTrue(self.api.is_book_available(self.book))

    def test_is_book_available_false(self):
      def check_input(url):
       if url == "XXhttp://openlibrary.org/search.json?q="+self.book+"XX":
           return self.json_data
       else:
           None
      self.api.make_request = Mock(side_effect=check_input)
      self.assertFalse(self.api.is_book_available(self.book))

    def test_is_book_available_none(self):
      def check_input(url):
       if url == "None":
           return self.json_data
       else:
           None
      self.api.make_request = Mock(side_effect=check_input)
      self.assertFalse(self.api.is_book_available(self.book))
    
    def test_books_by_author(self):
      self.api.make_request = Mock(return_value=self.json_author_data)
      the_list = self.api.books_by_author(self.book_author)
      self.assertEqual(the_list, self.data_books_by_author)

    def test_get_book_info(self):
      self.api.make_request = Mock(return_value=self.json_data)
      self.assertEqual(self.api.get_book_info(self.book), self.data_get_book_info)
    
    def test_get_ebooks(self):
        self.api.make_request = Mock(return_value=self.json_data)
        self.assertEqual(self.api.get_ebooks(self.book), self.data_get_ebooks)
    
    def test_request_url_books_by_author(self):
       self.api.make_request = Mock(return_value=[])
       self.api.books_by_author(self.book_author)
       self.api.make_request.assert_called_with("http://openlibrary.org/search.json?author=Nick Mason")
    
    def test_get_book_info_valid_url(self):
       self.api.make_request = Mock(return_value=[])
       self.api.get_book_info(self.book)
       self.api.make_request.assert_called_with("http://openlibrary.org/search.json?q=learning python")

    def test_get_ebooks_valid_url(self):
       self.api.make_request = Mock(return_value=[])
       self.api.get_ebooks(self.book)
       self.api.make_request.assert_called_with("http://openlibrary.org/search.json?q=learning python")