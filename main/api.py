from flask import request, jsonify
from flask_restful import Resource
from main.models import Book

books = {}

class Books(Resource):
    def post(self):
        user_input = request.get_json()

        if user_input == {} or user_input == None:
            return {"message":"error, inputs cannot be empty"}, 400
        if not "title" in user_input:
            return {"message":"error, book must have a title"}, 400
        if not "author" in user_input:
            return {"message":"error, book must have an author"}, 400
        if type(user_input["title"]) != str:
            return {"message":"error, title must be a string"}, 400

         # check if title characters is more than one
        if len(user_input["title"]) == 1: 
            return {"message":"error, book title must have more than one character"}, 400
        if len(user_input["author"]) == 1: 
            return {"message":"error, book author must have more than one character"}, 400

        # check if book is already in dictionary#
        if user_input["title"] in books:
            return {"message":"error, book is already in the library"}, 400
            
        #create a new book      
        title = user_input["title"]
        author = user_input["author"]
        id = len(books) + 1
        new_book = Book(title, author, id)

        #store book
        books[title] = new_book

        # serialize response, take value of objects and place into dict
        response = {}
        response["id"] = new_book.id
        response["title"] = new_book.title
        response["author"] = new_book.author

        return {"data" : response, "message": "new book successfully created"}, 201
    
    def get(self,bookId):
        if bookId == 0:
            return {"message":"error, book id cannot be zero"}, 400

        for book in books.values():
            if book.id == bookId:
                response = {}
                response["id"] = book.id
                response["title"] = book.title
                response["author"] = book.author 

                return {"selection": response, "message":"successfuly got book requested"}, 200

    def put(self, bookId):
        if bookId == 0:
            return {"message":"error, book id cannot be zero"}, 400

        for book in books.values():
            user_input = request.get_json()

            # validating inputed data
            if not "author" in user_input:
                return {"message":"error, book must have an author"}, 400
            if not "title" in user_input:
                return {"message":"error, book must have a title"}, 400

            if book.id == bookId:
                book.title = user_input["title"]
                book.author = user_input["author"]

                updated_book = {}
                updated_book["id"] = book.id
                updated_book["title"] = book.title
                updated_book["author"] = book.author

                return {"data":updated_book, "message":"book has been updated"}, 200


        
