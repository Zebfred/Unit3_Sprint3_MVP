from flask import Flask, render_template, request
from flask_sqlachemy import SQLAlchemy
import requests 

#Global variable
APP = Flask(__name__)
FLASK_ENV = "development"

APP.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///db.sqlite3'

DB = SQ

@APP.route("/", methods = ["POST", "GET"])

#function

def home():
    return render_template('home.html', title='dog picture', picture = randomImage())       

def randomImage(number=1):
    if number == 1:
        r=requests.get('https://dog.ceo/api/breeds/image/random')
    elif number <=50:
        r=requests.get('https://dog.ceo/api/breeds/image/random/'+str(number))
    else:
        raise ValueError('Max Number of Dogs Returned is 50')
    pics=r.json()['message']
    return pics


@APP.route("/breeds")
 
def breeds_list():
    return render_template('breed_list.html', all_breeds = listBreeds())

def listBreeds():
    r=requests.get('https://dog.ceo/api/breeds/list/all')
    b=r.json()
    breeds=[]

    for key, value in b['message'].items():
        if len(value)==0:
            breeds.append(key)
        else:
            for breed in value:
                full= breed + ' ' + key
                breeds.append(full)
    return breeds

@APP.route('/favorites', methods= ['POST'])
def favorites():
    faves= Dog.query.with_entirities
    faves=faves 

@APP.route('/saved',methods = ["POST"])
def saved():
    dog_url = request.values["URL"]
    breed = dog_url.split('/')[4]
    DB.session.add(Dog(url=dog, breed=breed))
    DB.session.commit()
    return render_template('home.html', picture= randomImage())

@APP.route('/reset')


def reset():
    DB.drop_all()
    DB.create_all()
    return "DB reset"


class Dog(DB.Model):
    
    id = DB.Column(DB.Integer,primary_key=True)
    url= DB.Column(DB.String(100))
    breed = DB.Column(DB.String(50))
    
    

if __name__ == "__main__":
    APP.run()



