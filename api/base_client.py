import time
import allure
import requests
from requests.exceptions import ReadTimeout, ConnectionError

class BaseClient:
    def __init__(self, base_url: str, timeout: int = 10, retries: int = 4, backoff_sec: float = 1.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.backoff_sec = backoff_sec
        self.session = requests.Session()

    def _url(self, path: str):
        return f"{self.base_url}{path}"

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = self._url(path)
        kwargs.setdefault("timeout", self.timeout)
        last_exc = None

        for attempt in range(1, self.retries + 1):
            with allure.step(f"{method.upper()} {url} (attempt {attempt}/{self.retries})"):
                try:
                    response = self.session.request(method, url, **kwargs)
                    allure.attach(str(response.status_code), "status_code", allure.attachment_type.TEXT)
                    allure.attach(response.text, "response_text", allure.attachment_type.TEXT)
                    return response
                except (ReadTimeout, ConnectionError, TimeoutError) as exc:
                    last_exc = exc
                    allure.attach(str(exc), "request_error", allure.attachment_type.TEXT)
                    if attempt < self.retries:
                        time.sleep(self.backoff_sec * attempt)
                    else:
                        raise last_exc