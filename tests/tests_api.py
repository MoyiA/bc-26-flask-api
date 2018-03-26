import unittest
import json
from main.app import create_app

class BooksTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.app_context = self.app.app_context() #create environment to handle our request
        self.app_context.push()
        self.postman = self.app.test_client() #used to send request to app(GET,POST,PUT,DELETE)
    
    def tearDown(self):
        self.app_context.pop()

    def test_not_empty_input(self):
        user_data = {}
        user_data_json = json.dumps(user_data) #turn user_data input into json data

        response = self.postman.post("/api/v1/books", data=user_data_json, content_type="application/json")
        self.assertEqual(400, response.status_code)
        
        data = response.get_data()
        api_response = json.loads(data) #turn json data from server into a dict
        self.assertEqual({"message":"error, inputs cannot be empty"}, api_response)

    def test_emtpty_title_input(self):
        user_data = {"author":"Sun Tzu"}
        user_data_json = json.dumps(user_data) #turnuser_data into json data

        response = self.postman.post("/api/v1/books", data=user_data_json, content_type="application/json")
        self.assertEqual(400, response.status_code)

        data = response.get_data()
        api_response = json.loads(data)
        self.assertEqual({"message":"error, book must have a title"}, api_response)

    def test_empty_author_input(self):
        user_data = {"title":"Art of War"}
        user_data_json = json.dumps(user_data)

        response = self.postman.post("/api/v1/books", data=user_data_json, content_type="application/json")
        self.assertEqual(400, response.status_code)
        
        data = response.get_data()
        api_response = json.loads(data)
        self.assertEqual({"message":"error, book must have an author"}, api_response)
    
    def test_title_length(self):
        user_data = {"title":"a", "author":"Sun Tzu"}
        user_data_json = json.dumps(user_data)

        response = self.postman.post("/api/v1/books", data=user_data_json, content_type="application/json")
        self.assertEqual(400, response.status_code)

        data = response.get_data()
        api_response = json.loads(data)
        self.assertEqual({"message":"error, book title must have more than one character"}, api_response)

    def test_author_length(self):
        user_data = {"title":"Art of War", "author":"S"}
        user_data_json = json.dumps(user_data)

        response = self.postman.post("/api/v1/books", data=user_data_json, content_type="application/json")
        self.assertEqual(400, response.status_code)

        data = response.get_data()
        api_response = json.loads(data)
        self.assertEqual({"message":"error, book author must have more than one character"}, api_response)

    def test_add_book(self):
        user_data = {"title":"Art of War", "author":"Sun Tzu"}
        user_data_json = json.dumps(user_data)

        response = self.postman.post("/api/v1/books", data=user_data_json, content_type="application/json")
        self.assertEqual(201, response.status_code)

        data = response.get_data()
        api_response = json.loads(data)
        self.assertEqual({"data": {
                                    "id": 1,
                                    "title": "Art of War",
                                    "author": "Sun Tzu"
                                },
                                "message": "new book successfully created"
                        }, api_response)

    def test_dulpicates(self):
        user_data = {"title":"Art of War", "author":"Sun Tzu"}
        user_data_json = json.dumps(user_data)

        response = self.postman.post("/api/v1/books", data=user_data_json, content_type="application/json")
        self.assertEqual(400, response.status_code)

        data = response.get_data()
        api_response = json.loads(data)
        self.assertEqual({"message":"error, book is already in the library"}, api_response)


