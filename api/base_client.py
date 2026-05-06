import time
import allure
import requests
from requests.exceptions import ReadTimeout, ConnectionError

class BaseClient: #базовый класс от него наследуются все клиенты куры заказы
    def __init__(self, base_url: str, timeout: int = 10, retries: int = 4, backoff_sec: float = 1.0): #задаем адрес API сколько ждать сколько пробывать пауза между пытками:)))
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.backoff_sec = backoff_sec
        self.session = requests.Session()

    def _url(self, path: str): #склейка как в старом добром postman и через него тоже на всякий проверю
        return f"{self.base_url}{path}"

    def request(self, method: str, path: str, **kwargs): # сердце: что то умное посовету друзей
        url = self._url(path)
        kwargs.setdefault("timeout", self.timeout)
        last_exc = None

        for attempt in range(1, self.retries + 1): # несколько попыток
            with allure.step(f"{method.upper()} {url} (attempt {attempt}/{self.retries})"): #логирование наверное полезно
                try:
                    response = self.session.request(method, url, **kwargs) # запрос - интересно когда мне это надоест
                    allure.attach(str(response.status_code), "status_code", allure.attachment_type.TEXT) # для логов полезно
                    allure.attach(response.text, "response_text", allure.attachment_type.TEXT)           # клавдия конечно аттачей мне подкинула ну пусть удет так
                    return response
                except (ReadTimeout, ConnectionError, TimeoutError) as exc:
                    last_exc = exc
                    allure.attach(str(exc), "request_error", allure.attachment_type.TEXT)
                    if attempt < self.retries:
                        time.sleep(self.backoff_sec * attempt)  #теперь я понял почему таймаут 10 секунд длится 30 секунды бэкоффы (спасибо нейронке за эту хрень в коде)
                    else:
                        raise last_exc # все плохо