from flask import Flask, request, jsonify
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# end point to test
@app.route("/")
def index():
    info = " Selamat datang di Planet API \n Info yang diberikan adalah diameter, massa, jarak orbit, periode, dan suhu permukaan \n Silakan akses /api/planet untuk info"
    return (info)

# end point to planets
@app.route("/api/planet")
def planet():
    planets = {
        "access route": "/api/planet",
        "params": "/{name_of_planet}"
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
    return jsonify(profile_mars)

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
    return jsonify(profile_mercury)

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
    # return api_schema.jsonify(profile_venus)
    return jsonify(profile_venus)

# endpoint to planet earth
@app.route("/api/planet/earth")
def earth():
    profile_earth = {
        # polar diameter
        "diameter": "12,714 km",
        "mass": "5.97 x 10^24 kg",
        "distance": "149,598,262",
        "period": "365.24 days",
        "temperature": "-88 to 58 celcius"
    }
    return jsonify(profile_earth)

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
    return jsonify(profile_jupiter)

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
    return jsonify(profile_saturn)

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
    return jsonify(profile_uranus)

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
    return jsonify(profile_neptune)

if __name__ == '__main__':
    app.run(debug=True)

# ----------------------------------------- #
# from flask_marshmallow import Marshmallow

# ma = Marshmallow(app)

# class Schema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ('diameter', 'mass', 'distance', 'period', 'temperature')

# api_schema = Schema()