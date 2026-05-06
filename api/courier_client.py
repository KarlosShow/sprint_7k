import allure
from api.base_client import BaseClient
from data.urls import COURIER_CREATE, COURIER_LOGIN, COURIER_DELETE

class CourierClient(BaseClient):

    @allure.step("Создать курьера")
    def create_courier(self, payload: dict):
        return self.request("POST", COURIER_CREATE, json=payload)

    @allure.step("Логин курьера")
    def login_courier(self, payload: dict):
        return self.request("POST", COURIER_LOGIN, json=payload)

    @allure.step("Удалить курьера")
    def delete_courier(self, courier_id: int):
        path = COURIER_DELETE.format(courier_id=courier_id)
        return self.request("DELETE", path)