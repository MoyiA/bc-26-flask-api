# Hello_books_api

Hello books is a library management application developed using Flask RESTful api. The app aid in management of library activities such as stocking, tracking of books and also renting out books to users.

## Dependancies

- Python3.
- Flask RESTful - An extension of the flask microframework.
- Virtualenv used to create a virtual environment separate from your computer system.

## Installation
First ensure python 3 is installed to your computer. Check here on how to install;
   https://www.python.org/

Next create and activate virtual envrionment on your machine;
   $ virtualenv myproject
   $ myproject\Scripts\activate

Install all the requirements needed:
   $ pip install -r requirements.txt

Pip install pylint to enable you to import from other libraries, and also pip install flask restful and other
libraries you my want to extend to your Api. 

## Getting Started

To run on the app on your local computer, git clone the project's url to your machine by copying the following
url and pasting it to the terminal prompt of your machine, downloading the project locally.

 $ git clone https://github.com/MoyiA/bc-26-flask-api.git

## Api
 It has the following endpoints so far implemented: 
   - POST /api/v1/books  Add a new book
   - PUT /api/v1/books/<bookId>  edit book info  
   - DELETE /api/v1/books/<bookId>  delete a book
   - GET /api/v1/books/ get a book
   - GET /api/v1/books/<bookId> get all books
    

# License handshake    
- This project is licensed under the MIT License - see the LICENSE.md file for details

# Authors books
- Anthony Moyi
