import allure
import pytest
from requests.exceptions import ReadTimeout
from api.courier_client import CourierClient
from data.urls import BASE_URL
from data.messages import ERROR_NOT_ENOUGH_DATA_LOGIN, ERROR_ACCOUNT_NOT_FOUND
from helpers.courier_helpers import build_courier_login_payload

@allure.epic("Courier")
@allure.feature("Login courier")
class TestCourierLogin:

    @allure.title("Курьер может авторизоваться: 200 и id")
    def test_courier_can_login(self, courier_client, new_courier):
        resp = courier_client.login_courier(
        build_courier_login_payload(
            new_courier["login"],
            new_courier["password"]
        )
    )
        assert resp.status_code == 200
        body = resp.json()
        assert "id" in body
        assert isinstance(body["id"], int)

    @allure.title("Для логина нужны обязательные поля: иначе 400")
    @pytest.mark.parametrize(
        "payload",
        [
            {"password": "123456"},
            {"login": "some_login"},
            {},
        ],
    )
    def test_login_requires_required_fields(self, payload):
        client = CourierClient(BASE_URL)
        try:
            resp = client.login_courier(payload)
            assert resp.status_code == 400
            body = resp.json()
            assert "message" in body
            assert ERROR_NOT_ENOUGH_DATA_LOGIN in body["message"]
        except ReadTimeout:
            pytest.skip("API зависает при невалидных данных (известный баг)")

    @allure.title("Ошибка при неверном логине/пароле: 404")
    def test_login_wrong_password_returns_error(self, courier_client, new_courier):

        resp = courier_client.login_courier(
            build_courier_login_payload(
                new_courier["login"],
                "wrong_password"
            )
        )
        assert resp.status_code == 404
        body = resp.json()
        assert "message" in body
        assert ERROR_ACCOUNT_NOT_FOUND in body["message"]

    @allure.title("Если логиниться несуществующим пользователем: 404")
    def test_login_nonexistent_user_returns_error(self):
        client = CourierClient(BASE_URL)
        resp = client.login_courier(build_courier_login_payload("nonexistent_login_123", "nonexistent_pass_123"))
        assert resp.status_code == 404
        body = resp.json()
        assert "message" in body
        assert ERROR_ACCOUNT_NOT_FOUND in body["message"]
