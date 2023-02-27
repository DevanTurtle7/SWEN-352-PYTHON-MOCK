import sys
sys.path.append('.')

from library import ext_api_interface
import json


class GetData:
    def __init__(self):
        self.api = ext_api_interface.Books_API()

    def get_ebooks(self, book):
        print("get ebooks: " + book)
        ebooks = self.api.get_ebooks(book)
        print(ebooks)
        with open('tests_data/ebooks.txt', 'w') as f:
            f.write(json.dumps(ebooks))

    def get_json(self, book):
        request_url = "%s?q=%s" % (self.api.API_URL, book)
        json_data = self.api.make_request(request_url)
        print(json_data)
        with open('tests_data/json_data.txt', 'w') as f:
            f.write(json.dumps(json_data))

    def get_json_author(self, author):
        request_url = "%s?author=%s" % (self.api.API_URL, author)
        json_author_data = self.api.make_request(request_url)
        print(json_author_data)
        with open('tests_data/json_author_data.txt', 'w') as f:
            f.write(json.dumps(json_author_data))

    def is_book_available(self, book):
        print("is book available: " + book)
        availability = self.api.is_book_available(book)
        print(availability)
        with open('tests_data/availability.txt', 'w') as f:
            f.write(json.dumps(availability))

    def books_by_author(self, author):
        print("books by author: " + author)
        books_by_author = self.api.books_by_author(author)
        print(books_by_author)
        with open('tests_data/books_by_author.txt', 'w') as f:
            f.write(json.dumps(books_by_author))

    def get_book_info(self, book):
        print("get book info: " + book)
        get_book_info = self.api.get_book_info(book)
        print(get_book_info)
        with open('tests_data/get_book_info.txt', 'w') as f:
            f.write(json.dumps(get_book_info))
        
    

if __name__ == "__main__":
    print("Getting Data...")
    getdata = GetData()
    getdata.get_ebooks('learning python')
    getdata.get_json('learning python')
    getdata.get_json_author('Nick Mason')
    getdata.is_book_available('learning python');
    getdata.books_by_author('Nick Mason');
    getdata.get_book_info('learning python');
