============================= test session starts ============================== 
platform win32 -- Python 3.14.2, pytest-9.0.3, pluggy-1.6.0 -- c:\Users\Сергей\sprint_7k\.venv\Scripts\python.exe
cachedir: .pytest_cache 
rootdir: C:\Users\Сергей\sprint_7k
plugins: allure-pytest-2.16.0
collected 15 items                                                                
 
tests/test_courier_create.py::TestCourierCreate::test_create_courier_success PASSED [  6%]
tests/test_courier_create.py::TestCourierCreate::test_cannot_create_duplicate_courier PASSED [ 13%] 
tests/test_courier_create.py::TestCourierCreate::test_create_courier_missing_required_field_returns_error[login] PASSED [ 20%] 
tests/test_courier_create.py::TestCourierCreate::test_create_courier_missing_required_field_returns_error[password] PASSED [ 26%] 
tests/test_courier_login.py::TestCourierLogin::test_courier_can_login PASSED [ 33%]
tests/test_courier_login.py::TestCourierLogin::test_login_requires_required_fields[payload0] PASSED [ 40%] 
tests/test_courier_login.py::TestCourierLogin::test_login_requires_required_fields[payload1] SKIPPED [ 46%] 
tests/test_courier_login.py::TestCourierLogin::test_login_requires_required_fields[payload2] SKIPPED [ 53%] 
tests/test_courier_login.py::TestCourierLogin::test_login_wrong_password_returns_error PASSED [ 60%] 
tests/test_courier_login.py::TestCourierLogin::test_login_nonexistent_user_returns_error PASSED [ 66%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[colors0] PASSED [ 73%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[colors1] PASSED [ 80%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[colors2] PASSED [ 86%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[None] PASSED [ 93%] 
tests/test_orders_list.py::TestOrdersList::test_orders_list_returns_orders PASSED 
[100%]

=================== 13 passed, 2 skipped in 125.11s (0:02:05) ===================
Найдено два бага в test_courier_login при невалидных данных сервер зависает вместо того чтобы прислать 400 bad request. Поэтому ставлю skipped по таймауту 10.

после ревью

tests/test_courier_create.py::TestCourierCreate::test_create_courier_success PASSED [  6%]
tests/test_courier_create.py::TestCourierCreate::test_cannot_create_duplicate_courier PASSED [ 13%] 
tests/test_courier_create.py::TestCourierCreate::test_create_courier_missing_required_field_returns_error[login] PASSED [ 20%] 
tests/test_courier_create.py::TestCourierCreate::test_create_courier_missing_required_field_returns_error[password] PASSED [ 26%] 
tests/test_courier_login.py::TestCourierLogin::test_courier_can_login PASSED [ 33%]
tests/test_courier_login.py::TestCourierLogin::test_login_requires_required_fields[payload0] XPASS [ 40%] 
tests/test_courier_login.py::TestCourierLogin::test_login_requires_required_fields[payload1] XFAIL [ 46%] 
tests/test_courier_login.py::TestCourierLogin::test_login_requires_required_fields[payload2] XFAIL [ 53%] 
tests/test_courier_login.py::TestCourierLogin::test_login_wrong_password_returns_error PASSED [ 60%] 
tests/test_courier_login.py::TestCourierLogin::test_login_nonexistent_user_returns_error PASSED [ 66%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[colors0] PASSED [ 73%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[colors1] PASSED [ 80%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[colors2] PASSED [ 86%] 
tests/test_orders_create.py::TestOrdersCreate::test_create_order_with_colors_parametrized[None] PASSED [ 93%] 
tests/test_orders_list.py::TestOrdersList::test_orders_list_returns_orders PASSED 
[100%]

============= 12 passed, 2 xfailed, 1 xpassed in 123.93s (0:02:03) ============== 
(.venv) PS C:\Users\Сергей\sprint_7k>  