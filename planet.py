from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
ma = Marshmallow(app)
basedir = os.path.abspath(os.path.dirname(__file__))

class Schema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('diameter', 'mass', 'distance', 'period', 'temperature')

api_schema = Schema()

# end point to planets
@app.route("/api/planet")
def planet():
    planets = {
        "Mars": {
            "diameter": "6,752 km",
            "mass": "6.42 x 10^23 kg",
            "distance": "227,943,824 km",
            "period": "687 days",
            "temperature": "-153 to 20 celcius"
        },
        "Mercury": {
            "diameter": "4,879 km",
            "mass": "3.30 x 10^23 kg",
            "distance": "57,909,227 km",
            "period": "88 days",
            "temperature": "-173 to 427 celcius"
        },
        "Venus": {
            "diameter": "12,104 km",
            "mass": "4.87 x 10^24 kg",
            "distance": "108,209,475 km",
            "period": "225 days",
            "temperature": "462 celcius"
        },
        "Earth": {
            "diameter": "12,714 km",
            "mass": "5.97 x 10^24 kg",
            "distance": "-",
            "period": "365.24 days",
            "temperature": "-88 to 58 celcius"
        },
        "Jupiter": {
            "diameter": "133,709 km",
            "mass": "1.90 x 10^27 kg",
            "distance": "778,340,821 km",
            "period": "4,333 days",
            "temperature": "-148 celcius"
        },
        "Saturn": {
            "diameter": "108,728 km",
            "mass": "5.68 x 10^26 kg",
            "distance": "1,426,666,422 km",
            "period": "10,756",
            "temperature": "-178 celcius"
        },
        "Uranus": {
            "diameter": "49,946 km",
            "mass": "8.68 x 10^25 kg",
            "distance": "2,870,658,186 km",
            "period": "30,687 days",
            "temperature": "-216 celcius"
        },
        "Neptune": {
            "diameter": "48,682 km",
            "mass": "1.02 x 10^26 kg",
            "distance": "4,498,396,441 km",
            "period": "60,190 days",
            "temperature": "-214 celcius"
        }
    }
    return jsonify(planets)

# ----------------------------------------- #

# endpoint to planet mars
@app.route("/api/planet/mars")
def mars():
    profile_mars = {
        # polar diameter
        "diameter": "6,752 km",
        "mass": "6.42 x 10^23 kg",
        "distance": "227,943,824 km",
        "period": "687 days",
        "temperature": "-153 to 20 celcius"
    }
    return api_schema.jsonify(profile_mars)

# endpoint to planet mercury
@app.route("/api/planet/mercury")
def mercury():
    profile_mercury = {
        # polar diameter
        "diameter": "4,879 km",
        "mass": "3.30 x 10^23 kg",
        "distance": "57,909,227 km",
        "period": "88 days",
        "temperature": "-173 to 427 celcius"
    }
    return api_schema.jsonify(profile_mercury)

# endpoint to planet venus
@app.route("/api/planet/venus")
def venus():
    profile_venus = {
        # polar diameter
        "diameter": "12,104 km",
        "mass": "4.87 x 10^24 kg",
        "distance": "108,209,475 km",
        "period": "225 days",
        "temperature": "462 celcius"
    }
    return api_schema.jsonify(profile_venus)

# endpoint to planet earth
@app.route("/api/planet/earth")
def earth():
    profile_earth = {
        # polar diameter
        "diameter": "12,714 km",
        "mass": "5.97 x 10^24 kg",
        "distance": "-",
        "period": "365.24 days",
        "temperature": "-88 to 58 celcius"
    }
    return api_schema.jsonify(profile_earth)

# endpoint to planet jupiter
@app.route("/api/planet/jupiter")
def jupiter():
    profile_jupiter = {
        # polar diameter
        "diameter": "133,709 km",
        "mass": "1.90 x 10^27 kg",
        "distance": "778,340,821 km",
        "period": "4,333 days",
        "temperature": "-148 celcius"
    }
    return api_schema.jsonify(profile_jupiter)

# endpoint to planet saturn
@app.route("/api/planet/saturn")
def saturn():
    profile_saturn = {
        # polar diameter
        "diameter": "108,728 km",
        "mass": "5.68 x 10^26 kg",
        "distance": "1,426,666,422 km",
        "period": "10,756",
        "temperature": "-178 celcius"
    }
    return api_schema.jsonify(profile_saturn)

# endpoint to planet uranus
@app.route("/api/planet/uranus")
def uranus():
    profile_uranus = {
        # polar diameter
        "diameter": "49,946 km",
        "mass": "8.68 x 10^25 kg",
        "distance": "2,870,658,186 km",
        "period": "30,687 days",
        "temperature": "-216 celcius"
    }
    return api_schema.jsonify(profile_uranus)

# endpoint to planet neptune
@app.route("/api/planet/neptune")
def neptune():
    profile_neptune = {
        # polar diameter
        "diameter": "48,682 km",
        "mass": "1.02 x 10^26 kg",
        "distance": "4,498,396,441 km",
        "period": "60,190 days",
        "temperature": "-214 celcius"
    }
    return api_schema.jsonify(profile_neptune)

if __name__ == '__main__':
    app.run(debug=True)

# ----------------------------------------- #
# 

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

# class UserSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ('username', 'email')


# user_schema = UserSchema()
# users_schema = UserSchema(many=True)


# # endpoint to create new user
# @app.route("/user", methods=["POST"])
# def add_user():
#     username = request.json['username']
#     email = request.json['email']
    
#     new_user = User(username, email)

#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify(new_user)


# # endpoint to show all users
# @app.route("/user", methods=["GET"])
# def get_user():
#     all_users = User.query.all()
#     result = users_schema.dump(all_users)
#     return jsonify(result.data)


# # endpoint to get user detail by id
# @app.route("/user/<id>", methods=["GET"])
# def user_detail(id):
#     user = User.query.get(id)
#     return user_schema.jsonify(user)


# # endpoint to update user
# @app.route("/user/<id>", methods=["PUT"])
# def user_update(id):
#     user = User.query.get(id)
#     username = request.json['username']
#     email = request.json['email']

#     user.email = email
#     user.username = username

#     db.session.commit()
#     return user_schema.jsonify(user)


# # endpoint to delete user
# @app.route("/user/<id>", methods=["DELETE"])
# def user_delete(id):
#     user = User.query.get(id)
    # db.session.delete(user)
    # db.session.commit()

    # return user_schema.jsonify(user)
