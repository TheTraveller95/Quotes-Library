import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from operator import itemgetter

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quotes_library'
app.config['MONGO_URI'] = 'mongodb+srv://root:r00tUser@myfirstcluster-p7dea.mongodb.net/quotes_library?retryWrites=true&w=majority'

mongo = PyMongo(app)

languages_list =[{"language_name":"English"},
{"language_name":"Abkhaz"},
{"language_name":"Adyghe"},
{"language_name":"Afrikaans"},
{"language_name":"Akan"},
{"language_name":"Albanian"},
{"language_name":"AmericanSignLanguage"},
{"language_name":"Amharic"},
{"language_name":"Arabic"},
{"language_name":"Aragonese"},
{"language_name":"Aramaic"},
{"language_name":"Armenian"},
{"language_name":"Assamese"},
{"language_name":"Aymara"},
{"language_name":"Balinese"},
{"language_name":"Basque"},
{"language_name":"Betawi"},
{"language_name":"Bosnian"},
{"language_name":"Breton"},
{"language_name":"Bulgarian"},
{"language_name":"Cantonese"},
{"language_name":"Catalan"},
{"language_name":"Cherokee"},
{"language_name":"Chickasaw"},
{"language_name":"Chinese"},
{"language_name":"Coptic"},
{"language_name":"Cornish"},
{"language_name":"Corsican"},
{"language_name":"CrimeanTatar"},
{"language_name":"Croatian"},
{"language_name":"Czech"},
{"language_name":"Danish"},
{"language_name":"Dutch"},
{"language_name":"Dawro"},
{"language_name":"Esperanto"},
{"language_name":"Estonian"},
{"language_name":"Ewe"},
{"language_name":"FijiHindi"},
{"language_name":"Filipino"},
{"language_name":"Finnish"},
{"language_name":"French"},
{"language_name":"Galician"},
{"language_name":"Georgian"},
{"language_name":"German"},
{"language_name":"Greek,Modern"},
{"language_name":"AncientGreek"},
{"language_name":"Greenlandic"},
{"language_name":"HaitianCreole"},
{"language_name":"Hawaiian"},
{"language_name":"Hebrew"},
{"language_name":"Hindi"},
{"language_name":"Hungarian"},
{"language_name":"Icelandic"},
{"language_name":"Indonesian"},
{"language_name":"Inuktitut"},
{"language_name":"Interlingua"},
{"language_name":"Irish"},
{"language_name":"Italian"},
{"language_name":"Japanese"},
{"language_name":"Javanese"},
{"language_name":"Kabardian"},
{"language_name":"Kalasha"},
{"language_name":"Kannada"},
{"language_name":"Kashubian"},
{"language_name":"Khmer"},
{"language_name":"Kinyarwanda"},
{"language_name":"Korean"},
{"language_name":"Kurdish/Kurdî"},
{"language_name":"Ladin"},
{"language_name":"Latgalian"},
{"language_name":"Latin"},
{"language_name":"Lingala"},
{"language_name":"Livonian"},
{"language_name":"Lojban"},
{"language_name":"LowerSorbian"},
{"language_name":"LowGerman"},
{"language_name":"Macedonian"},
{"language_name":"Malay"},
{"language_name":"Malayalam"},
{"language_name":"Mandarin"},
{"language_name":"Manx"},
{"language_name":"Maori"},
{"language_name":"MauritianCreole"},
{"language_name":"MiddleEnglish"},
{"language_name":"MiddleLowGerman"},
{"language_name":"MinNan"},
{"language_name":"Mongolian"},
{"language_name":"Norwegian"},
{"language_name":"OldArmenian"},
{"language_name":"OldEnglish"},
{"language_name":"OldFrench"},
{"language_name":"OldJavanese"},
{"language_name":"OldNorse"},
{"language_name":"OldPrussian"},
{"language_name":"Oriya"},
{"language_name":"Pangasinan"},
{"language_name":"Papiamentu"},
{"language_name":"Pashto"},
{"language_name":"Persian"},
{"language_name":"Pitjantjatjara"},
{"language_name":"Polish"},
{"language_name":"Portuguese"},
{"language_name":"Proto-Slavic"},
{"language_name":"Quenya"},
{"language_name":"Rajasthani"},
{"language_name":"RapaNui"},
{"language_name":"Romanian"},
{"language_name":"Russian"},
{"language_name":"Sanskrit"},
{"language_name":"Scots"},
{"language_name":"ScottishGaelic"},
{"language_name":"Semai"},
{"language_name":"Serbian"},
{"language_name":"Serbo-Croatian"},
{"language_name":"Slovak"},
{"language_name":"Slovene"},
{"language_name":"Spanish"},
{"language_name":"Sinhalese"},
{"language_name":"Swahili"},
{"language_name":"Swedish"},
{"language_name":"Tagalog"},
{"language_name":"Tajik"},
{"language_name":"Tamil"},
{"language_name":"Tarantino"},
{"language_name":"Telugu"},
{"language_name":"Thai"},
{"language_name":"TokPisin"},
{"language_name":"Turkish"},
{"language_name":"Twi"},
{"language_name":"Ukrainian"},
{"language_name":"UpperSorbian"},
{"language_name":"Urdu"},
{"language_name":"Uyghur"},
{"language_name":"Uzbek"},
{"language_name":"Venetian"},
{"language_name":"Vietnamese"},
{"language_name":"Vilamovian"},
{"language_name":"Volapük"},
{"language_name":"Võro"},
{"language_name":"Welsh"},
{"language_name":"Xhosa"},
{"language_name":"Yiddish"},
{"language_name":"Zazaki"},
{"language_name":"Zulu"}
]

love_quotes_list = [
{"quote_category":"Love",
"quote_text":"I have decided to stick with love. Hate is too great a burden to bear.",
"quote_author":"Martin Luther King, Jr.",
"quote_source":"Book",
"quote_source_name":"A Testament of Hope: The Essential Writings and Speeches",
"quote_language":"English"},
{"quote_category":"Love",
"quote_text":"Keep love in your heart. A life without it is like a sunless garden when the flowers are dead.",
"quote_author":"Oscar Wilde",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Love",
"quote_text":"En asuntos de amor, los locos son los que tienen más experiencia. De amor no preguntes nunca a los cuerdos; los cuerdos aman cuerdamente, que es como no haber amado nunca",
"quote_author":"Jacinto Benavente",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"Spanish"},
{"quote_category":"Love",
"quote_text":"El verdadero amor no es el amor propio, es el que consigue que el amante se abra a las demás personas y a la vida; no atosiga, no aísla, no rechaza, no persigue: solamente acepta",
"quote_author":"Antonio Gala",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"Spanish"},
{"quote_category":"Love",
"quote_text":"Hay quien ha venido al mundo para amar a una sola mujer y, consecuentemente, no es probable que tropiece con ella",
"quote_author":"José Ortega y Gasset.",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"Spanish"},
{"quote_category":"Love",
"quote_text":"Por eso juzgo y discierno, por cosa cierta y notoria, que tiene el amor su gloria a las puertas del infierno. ",
"quote_author":"Miguel de Cervantes",
"quote_source":"Book",
"quote_source_name":"La Galatea, 1585, Libro III",
"quote_language":"Spanish"}
]

mixed_quotes_list= [
{"quote_category":"Love",
"quote_text":"If your heart is a volcano, how shall you expect flowers to bloom?",
"quote_author":"Khalil Gibran",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Love",
"quote_text":"As the Father has loved me, so have I loved you.",
"quote_author":"Jesus Christ",
"quote_source":"Book",
"quote_source_name":"Bible",
"quote_language":"English"},
{"quote_category":"Love",
"quote_text":"Whatever our souls are made of, his and mine are the same.",
"quote_author":"Emily Bronte",
"quote_source":"Book",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Love",
"quote_text":"Gravitation is not responsible for people falling in love.",
"quote_author":"Albert Einstein",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Life",
"quote_text":"The purpose of our lives is to be happy.",
"quote_author":"Dalai Lama",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Life",
"quote_text":"Life is what happens when you’re busy making other plans.",
"quote_author":"John Lennon",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Life",
"quote_text":"You only live once, but if you do it right, once is enough.",
"quote_author":"Mae West",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Life",
"quote_text":"Many of life’s failures are people who did not realize how close they were to success when they gave up.",
"quote_author":"Thomas A. Edison",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Life",
"quote_text":"Never let the fear of striking out keep you from playing the game.",
"quote_author":"Babe Ruth",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Life",
"quote_text":"Money and success don’t change people; they merely amplify what is already there.",
"quote_author":"Will Smith",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Travel",
"quote_text":"The world is a book and those who do not travel read only a page.",
"quote_author":"Saint Augustine",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Travel",
"quote_text":"Not all those who wander are lost",
"quote_author":"J.R.R. Tolkien",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Travel",
"quote_text":"Life is either a daring adventure or nothing at all",
"quote_author":"Helen Keller",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Travel",
"quote_text":"Take only memories, leave only footprints",
"quote_author":"Chief Seattle",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"},
{"quote_category":"Travel",
"quote_text":"Never go on trips with anyone you do not love.",
"quote_author":"Hemmingway",
"quote_source":"N/A",
"quote_source_name":"N/A",
"quote_language":"English"}
]




@app.route('/')


def home():
    quotes=mongo.db.quotes.find()
    mylist = [] 
    """
    This part of the funsction has been usedfor creating a collection in mongodb with all the languages
    
    languages = mongo.db.languages
    for idiom in languages_list:
        languages.insert_one(idiom)
    """ 
    return render_template('home.html', 
    category=list(mongo.db.categories.find()),
    quotes=list(mongo.db.quotes.find()),
    sources=list(mongo.db.sources.find()),
    languages=list(mongo.db.languages.find().limit(50))
    # get_source=mylist_to_dict
    )

@app.route('/go_home')
def go_home():
    return redirect('home')

    
@app.route('/get_all_languages')
def get_all_languages():
    return render_template('home_two.html', 
    category=list(mongo.db.categories.find()),
    quotes=list(mongo.db.quotes.find()),
    sources=list(mongo.db.sources.find()),
    languages=list(mongo.db.languages.find())
    )


'''@app.route('/add_category')
def add_category():
    return render_template('addcategory.html',
    category=list(mongo.db.categories.find()))


@app.route('/create_category', methods=['POST'])
def create_category():
    category=mongo.db.categories
    category_list=list(mongo.db.categories.find())
    category.insert_one(request.form.to_dict())
    return redirect('home')'''
    

@app.route('/get_category/<category_id>')
def get_category(category_id):
    return render_template('getcategory.html', 
        category= list(mongo.db.categories.find()),
        categories=mongo.db.categories.find_one({'_id': ObjectId(category_id)}),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find()))



@app.route('/get_language/<language_id>') # modificar para que sea igual al get_source
def get_language(language_id):
    return render_template('getlanguage.html',
        language=mongo.db.languages.find_one({'_id': ObjectId(language_id)}),
        category= list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find()),
        languages=list(mongo.db.languages.find()))

@app.route('/get_source/<source_id>')
def get_source(source_id):
    return render_template('getsource.html',
        source=mongo.db.sources.find_one({'_id': ObjectId(source_id)}),
        category= list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find()))


@app.route('/create_quote')
def create_quote():
    return render_template('createquote.html',
    quotes=list(mongo.db.quotes.find()),
    category=list(mongo.db.categories.find()),
    sources=list(mongo.db.sources.find()),
    languages=list(mongo.db.languages.find()))

@app.route('/add_quote', methods=['POST'])
def add_quote():
    quote = mongo.db.quotes
    quote.insert_one(request.form.to_dict())
    return redirect(url_for('home'))


@app.route('/modify/<quote_id>')
def modify(quote_id):
    return render_template('modifyquote.html',
    quote=mongo.db.quotes.find_one({'_id': ObjectId(quote_id)}),
    category=list(mongo.db.categories.find()),
    sources=list(mongo.db.sources.find()),
    languages=list(mongo.db.languages.find()))

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
    return redirect('/home')

"""@app.route('/delete_quote/<quote_deleted_id>')
def delete_quote(quote_deleted_id):
    quote=mongo.db.quotes
    quote.delete_one({'_id': ObjectId(quote_deleted_id)})
    return redirect('/home')"""



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)