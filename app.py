from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__name__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Checkout(db.Model):
    """This is Checkout model containing unique ID, score to checkout and combo to achieve it"""
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    combo = db.Column(db.String(14), unique=True)

    def __init__(self, score, combo):
        self.score = score
        self.combo = combo
    
    def __repr__(self):
        return f'<Checkout {self.id} "{self.score}: {self.combo}">'

class CheckoutSchema(ma.Schema):
    """Schema containing important fields for Checkout"""
    class Meta:
        fields = ('id', 'score', 'combo')

checkout_schema = CheckoutSchema(strict=True)
checkouts_schema = CheckoutSchema(many=True, strict=True)

@app.route('/')
def index():
    """This is main request of this application containing instruction how to use it"""
    message = "Welcome to this simple Darts Checkout REST API!"
    return message

@app.route('/checkout', methods=['POST'])
def add_checkout():
    """Adds new checkout combination to database"""
    score = request.json['score']
    combo = request.json['combo']

    new_checkout = Checkout(score, combo)

    db.session.add(new_checkout)
    db.session.commit()

    return checkout_schema.jsonify(new_checkout)

@app.route('/checkout', methods=['GET'])
def get_all_checkouts():
    """Gets all checkouts stored in database"""
    all_checkouts = Checkout.query.all()
    result = checkouts_schema.dump(all_checkouts)

    return jsonify(result.data) 

@app.route('/checkout/id/<id>', methods=['GET'])
def get_checkout_by_id(id):
    """Gets specific checkout by given id"""
    checkout = Checkout.query.get(id)
    result = checkout_schema.dump(checkout)

    return jsonify(result.data)

@app.route('/checkout/score/<_score>', methods=['GET'])
def get_checkouts_for_score(_score):
    """Gets all checkouts stored in database matching given score"""
    checkouts = Checkout.query.filter_by(score = _score).all()
    result = checkouts_schema.dump(checkouts)

    return jsonify(result.data)

@app.route('/checkout/id/<id>', methods=['PUT'])
def update_checkout_with_id(id):
    """Updates fields for checkout with given id"""
    checkout = Checkout.query.get(id)

    score = request.json['score']
    combo = request.json['combo']

    checkout.score = score
    checkout.combo = combo

    db.session.commit()

    return checkout_schema.jsonify(checkout)

@app.route('/checkout/id/<id>', methods=['DELETE'])
def delete_checkout_by_id(id):
    """Deletes specific checkout by given id"""
    checkout = Checkout.query.get(id)
    db.session.delete(checkout)
    db.session.commit()

    return jsonify(result.data)

@app.route('/checkout', methods=['DELETE'])
def delete_all_checkouts():
    """Deletes all checkout combinations from database"""
    db.session.query(Checkout).delete()
    db.session.commit()

    return "Removed all checkouts from database"

def run_server(debug=False):
    app.run(debug=debug)

if __name__ == "__main__":
    run_server(debug=False)