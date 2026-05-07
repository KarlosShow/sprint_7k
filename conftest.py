#import pytest
#from api.courier_client import CourierClient
#from data.urls import BASE_URL
#from helpers.courier_helpers import create_courier_and_get_id
#
#@pytest.fixture
#def new_courier():
#   client = CourierClient(BASE_URL)
#    created = create_courier_and_get_id(client)
#    yield created 
#    client.delete_courier(created["id"])
import pytest
from api.courier_client import CourierClient
from data.urls import BASE_URL
from helpers.courier_helpers import (
    build_unique_courier_payload,
    build_courier_login_payload,
)


@pytest.fixture
def courier_client():
    return CourierClient(BASE_URL)


@pytest.fixture
def new_courier(courier_client):
    payload = build_unique_courier_payload()
    response = courier_client.create_courier(payload)
    assert response.status_code == 201
    yield payload
    login_payload = build_courier_login_payload(
        payload["login"],
        payload["password"]
    )
    login_response = courier_client.login_courier(login_payload)
    courier_id = login_response.json()["id"]
    courier_client.delete_courier(courier_id)


@pytest.fixture
def authorized_courier(courier_client, new_courier):
    login_payload = build_courier_login_payload(
        new_courier["login"],
        new_courier["password"]
    )
    response = courier_client.login_courier(login_payload)
    assert response.status_code == 200
    courier_id = response.json()["id"]
    return {
        "courier": new_courier,
        "id": courier_id
    }
