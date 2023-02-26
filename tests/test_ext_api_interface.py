import unittest
from unittest.mock import Mock, call
from library import library_db_interface

class TestLibbraryDBInterface(unittest.TestCase):

    def setUp(self):
        self.db_interface = library_db_interface.Library_DB()

    def test_insert_patron_not_in_db(self):
        patron_mock = Mock()
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        self.db_interface.db.insert = Mock(return_value=10)
        self.assertEqual(self.db_interface.insert_patron(patron_mock), 10)
    
    def test_insert_non_patron(self):
      non_patron = None;
      self.assertIsNone(self.db_interface.insert_patron(non_patron))
    
    def test_insert_patron_already_in_db(self):
      patron_mock = Mock()
      self.db_interface.retrieve_patron = Mock(return_value=patron_mock)
      self.assertEqual(self.db_interface.insert_patron(patron_mock), None)

    def test_get_patron_count(self):
      results = [Mock(), Mock(), Mock()]

      self.db_interface.db.all = Mock(return_value=results)
      self.assertEqual(self.db_interface.get_patron_count(), 3)
    
    def test_get_all_patrons(self):
      results = Mock()

      self.db_interface.db.all = Mock(return_value=results)
      self.assertEqual(self.db_interface.get_all_patrons(), results)

    def test_update_patron(self):
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        db_update_mock = Mock()
        self.db_interface.db.update = db_update_mock
        self.db_interface.update_patron(Mock())
        db_update_mock.assert_called()
    
    def test_update_patron_non_patron(self):
      non_patron = None
      self.assertEqual(self.db_interface.update_patron(non_patron), None)

    def test_convert_patron_to_db_format(self):
        patron_mock = Mock()

        patron_mock.get_fname = Mock(return_value=1)
        patron_mock.get_lname = Mock(return_value=2)
        patron_mock.get_age = Mock(return_value=3)
        patron_mock.get_memberID = Mock(return_value=4)
        patron_mock.get_borrowed_books = Mock(return_value=5)
        self.assertEqual(self.db_interface.convert_patron_to_db_format(patron_mock),
                         {'fname': 1, 'lname': 2, 'age': 3, 'memberID': 4,
                          'borrowed_books': 5})

    def test_retrieve_patron_none(self):
      self.db_interface.db.search = Mock(return_value=None)
      self.assertEqual(self.db_interface.retrieve_patron(10), None)
    
    def test_retrieve_patron_expected_fname(self):
      data = [{'fname': 'name', 'lname': 'name', 'age': 10, 'memberID': 2}]
      self.db_interface.db.search = Mock(return_value=data)
      self.assertEqual(self.db_interface.retrieve_patron(10).get_fname(), 'name')
    
    def test_retrieve_patron_expected_lname(self):
      data = [{'fname': 'name', 'lname': 'name', 'age': 10, 'memberID': 2}]
      self.db_interface.db.search = Mock(return_value=data)
      self.assertEqual(self.db_interface.retrieve_patron(10).get_lname(), 'name')

    def test_retrieve_patron_expected_age(self):
      data = [{'fname': 'name', 'lname': 'name', 'age': 10, 'memberID': 2}]
      self.db_interface.db.search = Mock(return_value=data)
      self.assertEqual(self.db_interface.retrieve_patron(10).get_age(), 10)

    def test_retrieve_patron_expected_memberID(self):
      data = [{'fname': 'name', 'lname': 'name', 'age': 10, 'memberID': 2}]
      self.db_interface.db.search = Mock(return_value=data)
      self.assertEqual(self.db_interface.retrieve_patron(10).get_memberID(), 2)
    
    def test_close_db(self):
      closeMock = Mock()
      self.db_interface.db.close = closeMock()
      self.db_interface.close_db()
      closeMock.assert_called_once()