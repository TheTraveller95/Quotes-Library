import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from operator import itemgetter

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quotes_library'
app.config['MONGO_URI'] = 'mongodb+srv://root:r00tUser@myfirstcluster-p7dea.mongodb.net/quotes_library?retryWrites=true&w=majority'

mongo = PyMongo(app)

languages_list = ["	English	",
"	Abkhaz	",
"	Adyghe	",
"	Afrikaans	",
"	Akan	",
"	Albanian	",
"	American Sign Language	",
"	Amharic	",
"	Arabic	",
"	Aragonese	",
"	Aramaic	",
"	Armenian	",
"	Assamese	",
"	Aymara	",
"	Balinese	",
"	Basque	",
"	Betawi	",
"	Bosnian	",
"	Breton	",
"	Bulgarian	",
"	Cantonese	",
"	Catalan	",
"	Cherokee	",
"	Chickasaw	",
"	Chinese	",
"	Coptic	",
"	Cornish	",
"	Corsican	",
"	Crimean Tatar	",
"	Croatian	",
"	Czech	",
"	Danish	",
"	Dutch	",
"	Dawro	",
"	Esperanto	",
"	Estonian	",
"	Ewe	",
"	Fiji Hindi	",
"	Filipino	",
"	Finnish	",
"	French	",
"	Galician	",
"	Georgian	",
"	German	",
"	Greek, Modern	",
"	Ancient Greek	",
"	Greenlandic	",
"	Haitian Creole	",
"	Hawaiian	",
"	Hebrew	",
"	Hindi	",
"	Hungarian	",
"	Icelandic	",
"	Indonesian	",
"	Inuktitut	",
"	Interlingua	",
"	Irish	",
"	Italian	",
"	Japanese	",
"	Javanese	",
"	Kabardian	",
"	Kalasha	",
"	Kannada	",
"	Kashubian	",
"	Khmer	",
"	Kinyarwanda	",
"	Korean	",
"	Kurdish/Kurdî	",
"	Ladin	",
"	Latgalian	",
"	Latin	",
"	Lingala	",
"	Livonian	",
"	Lojban	",
"	Lower Sorbian	",
"	Low German	",
"	Macedonian	",
"	Malay	",
"	Malayalam	",
"	Mandarin	",
"	Manx	",
"	Maori	",
"	Mauritian Creole	",
"	Middle English	",
"	Middle Low German	",
"	Min Nan	",
"	Mongolian	",
"	Norwegian	",
"	Old Armenian	",
"	Old English	",
"	Old French	",
"	Old Javanese	",
"	Old Norse	",
"	Old Prussian	",
"	Oriya	",
"	Pangasinan	",
"	Papiamentu	",
"	Pashto	",
"	Persian	",
"	Pitjantjatjara	",
"	Polish	",
"	Portuguese	",
"	Proto-Slavic	",
"	Quenya	",
"	Rajasthani	",
"	Rapa Nui	",
"	Romanian	",
"	Russian	",
"	Sanskrit	",
"	Scots	",
"	Scottish Gaelic	",
"	Semai	",
"	Serbian	",
"	Serbo-Croatian	",
"	Slovak	",
"	Slovene	",
"	Spanish	",
"	Sinhalese	",
"	Swahili	",
"	Swedish	",
"	Tagalog	",
"	Tajik	",
"	Tamil	",
"	Tarantino	",
"	Telugu	",
"	Thai	",
"	Tok Pisin	",
"	Turkish	",
"	Twi	",
"	Ukrainian	",
"	Upper Sorbian	",
"	Urdu	",
"	Uyghur	",
"	Uzbek	",
"	Venetian	",
"	Vietnamese	",
"	Vilamovian	",
"	Volapük	",
"	Võro	",
"	Welsh	",
"	Xhosa	",
"	Yiddish	",
"	Zazaki	"
]



@app.route('/')
def home():
    quotes=mongo.db.quotes.find()
    mylist = []
    #for quote in quotes: need to be reviewed because does not work. it should create a list with the values of the key quote_source and delete the doubles
     #   source = quote.get('quote_source') 
      #  source_list = mylist.append(source) 
    #mylist_to_dict = dict(mylist) 
    return render_template('home.html', 
    category=list(mongo.db.categories.find()),
    quotes=list(mongo.db.quotes.find())
    # get_source=mylist_to_dict
    )

@app.route('/add_category')
def add_category():
    return render_template('addcategory.html',
    category=mongo.db.categories.find())

@app.route('/create_category', methods=['POST'])
def create_category():
    category=mongo.db.categories
    category.insert_one(request.form.to_dict())
    return redirect('home')

@app.route('/get_category/<category_id>')
def get_category(category_id):
    return render_template('getcategory.html', 
        category= list(mongo.db.categories.find()),
        categories=mongo.db.categories.find_one({'_id': ObjectId(category_id)}),
        quotes=list(mongo.db.quotes.find()))

@app.route('/get_author/<author>')
def get_author(author):
    return render_template('getauthor.html',
        quote=list(mongo.db.quotes.find({'quote_author': author})),
        quote_author=author,
        category=list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()))

@app.route('/get_source/<source>')
def get_source(source):
    return render_template('getsource.html',
        quote=list(mongo.db.quotes.find({'quote_source': source})),
        quote_source=source,
        category= list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()))


@app.route('/create_quote')
def create_quote():
    return render_template('createquote.html',
    quote=list(mongo.db.quotes.find()),
    categories=list(mongo.db.categories.find()))

@app.route('/add_quote', methods=['POST'])
def add_quote():
    quote = mongo.db.quotes
    quote.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

@app.route('/modify/<quote_id>')
def modify(quote_id):
    return render_template('modifyquote.html',
    quote=mongo.db.quotes.find_one({'_id': ObjectId(quote_id)}),
    category=list(mongo.db.categories.find()))

@app.route('/modify_quote/<quote_id>', methods=['POST'])
def modify_quote(quote_id):
    quote = mongo.db.quotes
    quote.update({'_id': ObjectId(quote_id)}, {
        'quote_category': request.form.get('quote_category'),
        'quote_text': request.form.get('quote_text'),
        'quote_author': request.form.get('quote_author'),
        'quote_source': request.form.get('quote_source'),
        'quote_source_name': request.form.get('quote_source_name'),
        'quote_language': request.form.get('quote_language')
    })
    return redirect(url_for('home'))

@app.route('/delete_quote/<quote_id>')
def delete_quote(quote_id):
    quote=mongo.db.quotes
    quote.delete_one({'_id': ObjectId(quote_id)})
    return redirect('home')

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)