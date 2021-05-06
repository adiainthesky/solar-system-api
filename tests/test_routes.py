def test_get_all_planets_empty(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_planet(create_a_planet, client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"Earth",
        "description":"home",
        "distance from Earth":0
        }

def test_get_planet_empty(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None

def test_get_planets(create_a_planet, client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id":1,
        "name":"Earth",
        "description":"home",
        "distance from Earth":0
        }]