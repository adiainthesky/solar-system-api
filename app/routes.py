from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"])
    def handle_planets():
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    distance_from_earth=request_body["distance from Earth"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)