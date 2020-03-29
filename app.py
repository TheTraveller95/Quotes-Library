import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from operator import itemgetter
from dotenv import load_dotenv #added the .env and .gitignore

load_dotenv()

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quotes_library'
app.config['MONGO_URI'] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("secret_key")

mongo = PyMongo(app)

@app.route('/')


def home():
    """
    This function loads the home page
    """
    #quotes=mongo.db.quotes.find()
    #mylist = [] 

    return render_template('home.html', 
        category=list(mongo.db.categories.find()),
        #quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find().limit(50))
        )

@app.route('/go_home')
def go_home():
    return redirect('home')

    
@app.route('/get_all_languages')
def get_all_languages():
    """
    This function loads the full languages list on the home page
    """
    return render_template('home_two.html', 
        category=list(mongo.db.categories.find()), # I need all of them because are called inside the home_two.html
        quotes=list(mongo.db.quotes.find()), 
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find())
        )


@app.route('/get_category/<category_id>')
def get_category(category_id):
    """
    This function will load the getcategory.html that displays the quotes list depending on the chosen category
    """
    return render_template('getcategory.html', 
        category= list(mongo.db.categories.find()),
        categories=mongo.db.categories.find_one({'_id': ObjectId(category_id)}),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find())
        )



@app.route('/get_language/<language_id>') 
def get_language(language_id):
    """
    This function will load the getlanguage.html that displays the quotes list depending on the chosen language
    """
    return render_template('getlanguage.html',
        language=mongo.db.languages.find_one({'_id': ObjectId(language_id)}),
        category= list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find())
        )

@app.route('/get_source/<source_id>')
def get_source(source_id):
    """
    This function will load the getsource.html that displays the quotes list depending on the chosen source
    """
    return render_template('getsource.html',
        source=mongo.db.sources.find_one({'_id': ObjectId(source_id)}),
        category= list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find())
        )


@app.route('/quote/add', methods=['GET','POST'])
def create_quote():
    """
    This function will allow the user to add a new quote
    """
    if request.method == 'POST':
        quote = mongo.db.quotes
        quote.insert_one(request.form.to_dict())
        return redirect(url_for('home'))

    return render_template('createquote.html',
        quotes=list(mongo.db.quotes.find()),
        category=list(mongo.db.categories.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find())
        )


@app.route('/edit/<quote_id>', methods=['GET','POST'])
def modify(quote_id):
    """
    This function will allow the user to edit an existing quote
    """
    if request.method == 'POST':
        quote = mongo.db.quotes
        quote.update({'_id': ObjectId(quote_id)}, {
            'quote_category': request.form.get('quote_category'),
            'quote_text': request.form.get('quote_text'),
            'quote_author': request.form.get('quote_author'),
            'quote_source': request.form.get('quote_source'),
            'quote_source_name': request.form.get('quote_source_name'),
            'quote_language': request.form.get('quote_language')
        })
        return redirect(url_for('home'))  # cannot redirect to a differen

    return render_template('modifyquote.html',
        quote=mongo.db.quotes.find_one({'_id': ObjectId(quote_id)}),
        category=list(mongo.db.categories.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find()))



@app.route('/delete_quote/<quote_id>')
def delete_quote(quote_id):
    """
    This function will allow the user to edit an existing quote
    """
    quote=mongo.db.quotes
    quote.delete_one({'_id': ObjectId(quote_id)})
    flash("Quote deleted")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)