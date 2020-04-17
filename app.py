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
    Loads the home page
    """
    return render_template('home.html', 
        category=list(mongo.db.categories.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find().limit(50))
        )

@app.route('/go_home')
def go_home():
    """
    Redirect to the home page on mobile version
    """
    return redirect('home')

    
@app.route('/get_all_languages')
def get_all_languages():
    """
    Loads the full languages list on the home page
    """
    return render_template('home_two.html', 
        category=list(mongo.db.categories.find()), 
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find())
        )

@app.route('/get_less_languages')
def get_less_languages():
    """
    Loads the half languages list on the home page
    """
    return render_template('home.html', 
        category=list(mongo.db.categories.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find().limit(50))
        )


@app.route('/quote/category/<category_id>')
def get_quote_by_category(category_id):
    """
    Displays the quotes list depending on the chosen category
    """
    return render_template('getcategory.html', 
        category= list(mongo.db.categories.find()),
        categories=mongo.db.categories.find_one({'_id': ObjectId(category_id)}),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find()) # tried to delete this after having extended the base.html but does not work
        )



@app.route('/quote/language/<language_id>') 
def get_quote_by_language(language_id):
    """
    Displays the quotes list depending on the chosen language
    """
    return render_template('getlanguage.html',
        language=mongo.db.languages.find_one({'_id': ObjectId(language_id)}),
        quotes=list(mongo.db.quotes.find()),
        languages=list(mongo.db.languages.find())
        )

@app.route('/quote/source/<source_id>')
def get_quote_by_source(source_id):
    """
    Displays the quotes list depending on the chosen source
    """
    return render_template('getsource.html',
        source=mongo.db.sources.find_one({'_id': ObjectId(source_id)}),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find())
        )


@app.route('/quote/add', methods=['GET','POST'])
def create_quote():
    """
    Allow the user to add a new quote
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


@app.route('/quote/edit/<quote_id>', methods=['GET','POST'])
def modify(quote_id):
    """
    Allow the user to edit an existing quote
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
        return redirect(url_for('home'))  # cannot redirect to a different

    return render_template('modifyquote.html',
        quote=mongo.db.quotes.find_one({'_id': ObjectId(quote_id)}),
        category=list(mongo.db.categories.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find()))



@app.route('/quote/delete_quote/<quote_id>')
def delete_quote(quote_id):
    """
    Allow the user to delete an existing quote
    """
    quote=mongo.db.quotes
    quote.delete_one({'_id': ObjectId(quote_id)})
    flash("Quote deleted")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=os.getenv("DEBUG"))