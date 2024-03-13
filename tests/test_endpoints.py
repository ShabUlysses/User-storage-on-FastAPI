import json


def test_get_all_customers(app_client, create_customer):
    response = app_client.get(f"/customers")
    customer = response.json()

    assert customer == [create_customer.id]


def test_get_customer_by_id(app_client, create_customer):
    response = app_client.get(f"/customers/{create_customer.id}")
    customer = response.json()

    assert response.status_code == 200
    assert customer["email"] == "test@gmail.com"
    assert customer["name"] == "test_wayne"
    assert customer["city"] == "test"


def test_create_customer(app_client, db):
    data = {
        "name": "test_john",
        "city": "test_moscow",
        "email": "test2@gmail.com",
        "password": "ghasdfasd"
    }
    response = app_client.post(f"/create_customer", data=json.dumps(data))
    customer = response.json()

    assert response.status_code == 201
    assert customer["email"] == "test2@gmail.com"
    assert customer["name"] == "test_john"
    assert customer["city"] == "test_moscow"
