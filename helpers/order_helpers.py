import allure
from data.payloads import ORDER_CREATE_BASE

@allure.step("Собрать payload заказа с параметром colors")
def build_order_payload(colors):
    payload = ORDER_CREATE_BASE.copy()
    if colors is None:
        return payload
    payload["color"] = colors
    return payload