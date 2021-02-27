from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)

import requests
api = 'http://localhost:5002'

def new_register (generated):
        for key, value in generated.items(): 
            return key, value

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql_container:3306/flask-db'

db = SQLAlchemy(app)


class Duo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal= db.Column(db.String, nullable=False)
    prize = db.Column(db.String, nullable=False)
db.create_all() 

Duos = Duo.query.all()

@app.route('/')
def hello_internet():
    
    response = requests.get(api)
    generated = response.json() 
    print (generated)
    print(type(generated))

    animal, prize = new_register (generated)
    db.session.add(Duo(animal=animal, prize=prize))
    db.session.commit()
    
    final = Duo.query.all()
    for i in final: 
        animal1 = i.animal
        prize1 = i.prize 

    return render_template ( "base.html" , gn = (animal1, prize1))


if __name__=='__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')