import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quotes_library'
app.config['MONGO_URI'] = 'mongodb+srv://root:r00tUser@myfirstcluster-p7dea.mongodb.net/quotes_library?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def home():
    
    return render_template('home.html', 
    categories=mongo.db.categories.find(),
    quotes=list(mongo.db.quotes.find()),
    hola=hola())

def hola():
    quotes=mongo.db.quotes.find()
    output = []
    for quote in quotes:
        quote.quote_source
        output.push(quote.quote_source)
        mylist = list(dict.fromkeys(output))
    return(mylist)

def get_value():
    source = mongo.db.categories.find()

@app.route('/get_category/<category_id>')
def get_category(category_id):
    return render_template('getcategory.html', 
        category = mongo.db.categories.find_one({'_id': ObjectId(category_id)}),
        quotes=mongo.db.quotes.find())

@app.route('/get_author/<author>')
def get_author(author):
    return render_template('getauthor.html',
        quote=mongo.db.quotes.find({'quote_author': author}))

@app.route('/get_source/<source>')
def get_source(source):
    return render_template('getsource.html',
    quote=mongo.db.quotes.find({'quote_source': source}))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)