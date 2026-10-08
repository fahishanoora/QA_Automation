import requests

def test_get_user_list():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)


    assert response.status_code == 200


    data = response.json()

    assert data["page"] == 2
    assert len(data["data"]) > 0


def test_create_user():
    url = "https://reqres.in/api/users"

    user_payload = {
        "name": "Fahisha",
        "job": "QA automation Engineer"
    }

    response = requests.post(url, json=user_payload)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Fahisha"
    assert "id" in data 

def test_update_user():
    url = "https://reqres.in/api/users/2"

    update_payload = {
        "name": "Fahisha",
        "job": "Senior SDET Lead"
    }

    response = requests.put(url, json=update_payload)

    assert response.status_code == 200

    data = response.json()
    assert data["job"] == "Senior SDET Lead"

def test_delete_user():
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url)

    assert response.status_code == 204