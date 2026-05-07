import allure
from helpers.generators import random_lower_string
from data.payloads import COURIER_CREATE_TEMPLATE, COURIER_LOGIN_TEMPLATE

@allure.step("Сгенерировать уникальный payload курьера")
def build_unique_courier_payload():  #генерируем курьера
    payload = COURIER_CREATE_TEMPLATE.copy() # шаблон курьера потом заполяем случайностями
    payload["login"] = random_lower_string(10)
    payload["password"] = random_lower_string(10)
    payload["firstName"] = random_lower_string(10)
    return payload

@allure.step("Собрать payload логина курьера") # собираем тело для логина курьера
def build_courier_login_payload(login: str, password: str):
    payload = COURIER_LOGIN_TEMPLATE.copy()
    payload["login"] = login
    payload["password"] = password
    return payload

#@allure.step("Создать курьера и получить его id через логин") # создаем логинисмся достсаем id
#def create_courier_and_get_id(courier_client):
#    courier_payload = build_unique_courier_payload()
#    create_resp = courier_client.create_courier(courier_payload)
#    assert create_resp.status_code == 201, f"Courier create failed: {create_resp.status_code} {create_resp.text}"
#    login_payload = build_courier_login_payload(courier_payload["login"], courier_payload["password"])
#    login_resp = courier_client.login_courier(login_payload)
#    assert login_resp.status_code == 200, f"Courier login failed: {login_resp.status_code} {login_resp.text}"
#    courier_id = login_resp.json().get("id")
#   assert isinstance(courier_id, int), f"No courier id in response: {login_resp.text}"
#    return {"courier": courier_payload, "id": courier_id}
