def test_get_all_planets(client):
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