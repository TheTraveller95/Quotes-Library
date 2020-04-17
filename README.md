# The Quotes Library

The quote library is a place where people can find, add, modify or delete quotes coming from different authors, source or languages. 
In the today life, with the massive usage of the social networks, the quotes are becoming very important (if not fundamental) to express 
certain feelings or motivate people. 
In the Web can find quotes of all categories: motivationals, about life, sport, behaviour, travel, friends, family, etc.

## UX

This is basically the main goal of this project: give the users the opportunity of create a library with all the quotes taken by other outhors or created by themselves
and keep them in one single place.
The users will be able to browse them by category, language and source in order to make the research easier.

In order to see some of this project mockups, please find them inside the Mockups folder.

## Features

The frontend part of this project has been created in 9 HTML files, 1 JS file (containing some jQuery codes in order to activate the interactive menus) 
and 1 CSS file for styling the entire project.
The main HTML page is the one called base.html which contain the navbar and the footer. The others HTML files are all extensions (using Jinja templates) of that one.
For the backend part, I used a .py file where I started a Flask application using Pymongo. All the data have been stored in a database using MongoDB.
The entire project has been pushed to Heroku. For this reason 2 more files hav been generated: the Procfile and the requirements.txt

### Home page

The home page is an extension of the base.html file, which, as previously mentioned, contains the navbar and the footer. It is divided in 4 parts:

    - the article which explains the main of the project

    - the section from where the user can browse the quotes by category

    - the section from where the user can browse the quotes by language

    - the section from where the user can browse the quotes by source

### The getcategory, getlanguage and getsource pages

Those pages contain the same structure.

    - they will display the language, category or source as title depending on the user choise

    - they will retreive all the data that maches with the user's choise from the DB

    - they give to the user the option to edit or delete the quotes 

### The createquote.html and modifyquote.html page

In the createquote.html the user can create a brand new quote adding all the elements required (category, text, author, etc) and add it to the DB.
It can be accessed from the navbar present on any page

The modifyquote.html is very similar to the createquote.html but here the user can edit an existing quote. 
It can be accessed by clicking on the edit button present on every quote

## Existing Features

The most important part of this project is the possibility for the user to add, edit and delete items stored in the DB.
The user becomes the protagonist, being the one who is responsible of the creation and the maintenance of the library. This will grow depending on the users' interaction.
Some quotes have been already added by myself in order to test the efficency of all the integrated functions. 

## Technologies used

- Materialize
- Fontawesome
- jQuery
- Flask and Pymongo

## Testing

The first tests about the good website functionality have been done locally, using the Google Chrome tool. By using it I was able to test the 
project trough a large variety of devices in a responsive environment. Once everyhting looked good in the Chrome environmnet, the project has 
been tested in the others browsers (IE and Edge) The website has then been tested in differet physical devices (iPad, iPhone 8, iPhone 11 and 
Honor 9) and after the good feedback, it has been sent to multiple contacts in order to test it in more devices as possible. All of them have been 
given some specific tasks in order to test each one of the critical features of the project.
The main complain was that after having edited a quote, the website brought the user to the home page instead of to the previous quotes page
The issues have been solved succesfully. 
As well, some unit tests have been implemented to assure the correct application functionality.

## Deployment

The project deployment has been done using Heroku. The pubblic accessible web link of my project has been deployed by going to 
Heroku --> quote-library-app --> Settings --> scrolling down until Domains. There the pubblic link can be found https://quotes-library-app.herokuapp.com/

In order to run the code locally you need to go to https://github.com/TheTraveller95/quotes-library , click on the Clone or Download button. There you have 2 options, or download the zip directly 
or run the command "git clone https://github.com/TheTraveller95/quotes-library.git" in your machine's terminal after having navigated to the folder 
you want to save the code into.

## User's stories

- As an user, I can finally have all the quotes I need in only one place. I won't need to browse the entire web anymore

- As an author, I can add quotes from my books so everyone can use them and I'll get the oportunity of increasing my books sells 

- It is my favourite place where to get tue quotes from for all my social media profiles

## Credits

### Content

- The HTML and CSS code for the footer has been copied and rearranged from my previous project named Ecuador

### Media

- The background image of the entire webpage can be found here https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.alemdad.ly%2FSoul-Collection-Music-497931%2F&psig=AOvVaw2kBtvW9O4a0mbTIWCtbx-T&ust=1586094169769000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNDluLTzzugCFQAAAAAdAAAAABAD

## Acknowledgements

-   About the coding related technical knowledge, the https://www.w3schools.com and https://stackoverflow.com/ websites in addition to the help received from the Code Institute tutors and mentor really helped me a lot.
