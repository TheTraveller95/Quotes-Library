import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quotes_library'
app.config['MONGO_URI'] = 'mongodb+srv://root:r00tUser@myfirstcluster-p7dea.mongodb.net/quotes_library?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def hello():
    return render_template('home.html', categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)