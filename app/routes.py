from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = Planet.query.get(planet_id)

#     return {
#         "id": planet.id,
#         "title": planet.title,
#         "description": planet.description
#         "distance from Earth": planet.distance_from_earth
#     }


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():

    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "title": planet.title,
                "description": planet.description
                "distance from Earth": planet.distance_from_earth
            })

        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    distance_from_earth=request_body["distance from Earth"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)