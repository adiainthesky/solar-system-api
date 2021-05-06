import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def create_a_planet(app):
    Earth = Planet(name="Earth",
                      description="home",
                      distance_from_earth=0)

    db.session.add_all([Earth])
    db.session.commit()

# @pytest.fixture
# def post_a_planet(app):
#     Earth = Planet(name="Earth",
#                       description="home",
#                       distance_from_earth=0)

#     db.session.add_all([Earth])
#     db.session.commit()