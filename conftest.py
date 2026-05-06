import pytest
from api.courier_client import CourierClient
from data.urls import BASE_URL
from helpers.courier_helpers import create_courier_and_get_id

@pytest.fixture
def new_courier():
    client = CourierClient(BASE_URL)
    created = create_courier_and_get_id(client)
    yield created 
    client.delete_courier(created["id"])