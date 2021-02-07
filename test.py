import os
import unittest
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quotes_library'
app.config['MONGO_URI'] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("secret_key")

mongo = PyMongo(app)

class TestHome(unittest.TestCase):

    def test_quote_existence(self):

        """test the connection between the app and the DB. The quote below has been taken from the DB. Check if the app is able to retrive it"""

        a = mongo.db.quotes.find_one({'quote_category': "Love",
            'quote_text': "I have decided to stick with love. Hate is too great a burden to bear.",
            'quote_author': "Martin Luther King, Jr.",
            'quote_source': "Book",
            'quote_source_name': "A Testament of Hope: The Essential Writings and Speeches",
            'quote_language': "English"})

        b = mongo.db.quotes.find()

        self.assertIn(a, b)

    def test_quote_creation(self):

        """test creation of a new quote and its existence inside the DB"""

        def creation(methods=['POST']):
            a = mongo.db.quotes.find_one({'quote_category': "Life",
            'quote_text': "test",
            'quote_author': "test123",
            'quote_source': "Book",
            'quote_source_name': "test456",
            'quote_language': "English"})

            return a
        return (creation)
        
        c = a

        b = mongo.db.quotes.find()

        self.assertIn(c, b)

if __name__ == '__main__':
    unittest.main()