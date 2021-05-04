from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance from Earth": planet.distance_from_earth
        }
    
    elif request.method == "PUT":
            
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.distance_from_earth = form_data["distance from Earth"]

        db.session.commit()

        return jsonify(f"Planet #{planet.id} successfully updated") 

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet {planet.name} successfully deleted")



@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():

    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance from Earth": planet.distance_from_earth
            })

        return jsonify(planets_response), 201

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    distance_from_earth=request_body["distance from Earth"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)