import allure
from api.base_client import BaseClient
from data.urls import ORDERS_CREATE, ORDERS_LIST

class OrdersClient(BaseClient):

    @allure.step("Создать заказ")
    def create_order(self, payload: dict):
        return self.request("POST", ORDERS_CREATE, json=payload)

    @allure.step("Получить список заказов")
    def get_orders_list(self):
        return self.request("GET", ORDERS_LIST, timeout=30)