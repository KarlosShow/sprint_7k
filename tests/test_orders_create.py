import allure
import pytest
from api.orders_client import OrdersClient
from data.urls import BASE_URL
from helpers.order_helpers import build_order_payload

@allure.epic("Orders")
@allure.feature("Create order")
class TestOrdersCreate:

    @allure.title("Создание заказа: варианты цвета возвращают track")
    @pytest.mark.parametrize(
        "colors",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None,  
        ],
    )
    def test_create_order_with_colors_parametrized(self, colors):
        client = OrdersClient(BASE_URL)
        payload = build_order_payload(colors)
        resp = client.create_order(payload)
        assert resp.status_code == 201
        body = resp.json()
        assert "track" in body
        assert body["track"] is not None
