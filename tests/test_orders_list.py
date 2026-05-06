import allure
from api.orders_client import OrdersClient
from data.urls import BASE_URL

@allure.epic("Orders")
@allure.feature("Orders list")
class TestOrdersList:

    @allure.title("Получение списка заказов: тело ответа содержит список orders")
    def test_orders_list_returns_orders(self):
        client = OrdersClient(BASE_URL)
        resp = client.get_orders_list()
        assert resp.status_code == 200
        body = resp.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)
