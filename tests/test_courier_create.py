import allure
import pytest
from api.courier_client import CourierClient
from data.urls import BASE_URL
from data.messages import ERROR_NOT_ENOUGH_DATA_CREATE, ERROR_LOGIN_ALREADY_USED
from helpers.courier_helpers import build_unique_courier_payload, build_courier_login_payload

@allure.epic("Courier")
@allure.feature("Create courier")
class TestCourierCreate:

    @allure.title("Курьера можно создать: 201 и ok=true")
    def test_create_courier_success(self):
        client = CourierClient(BASE_URL)
        payload = build_unique_courier_payload()
        resp = client.create_courier(payload)
        assert resp.status_code == 201
        assert resp.json() == {"ok": True}
        login_resp = client.login_courier(build_courier_login_payload(payload["login"], payload["password"]))
        courier_id = login_resp.json().get("id")
        client.delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров: 409 и ошибка")
    def test_cannot_create_duplicate_courier(self):
        client = CourierClient(BASE_URL)
        payload = build_unique_courier_payload()
        first = client.create_courier(payload)
        assert first.status_code == 201
        assert first.json() == {"ok": True}
        second = client.create_courier(payload)
        assert second.status_code == 409
        body = second.json()
        assert "message" in body
        assert ERROR_LOGIN_ALREADY_USED in body["message"]
        login_resp = client.login_courier(build_courier_login_payload(payload["login"], payload["password"]))
        courier_id = login_resp.json().get("id")
        client.delete_courier(courier_id)

    @allure.title("Создание курьера требует обязательные поля login и password: иначе 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field_returns_error(self, missing_field):
        client = CourierClient(BASE_URL)
        payload = build_unique_courier_payload()
        payload.pop(missing_field)
        resp = client.create_courier(payload)
        assert resp.status_code == 400
        body = resp.json()
        assert "message" in body
        assert ERROR_NOT_ENOUGH_DATA_CREATE in body["message"]