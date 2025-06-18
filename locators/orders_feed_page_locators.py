from selenium.webdriver.common.by import By

# поле ввода Email
LOGIN_EMAIL = (By.XPATH, "//input[@name='name']")

# поле ввода Пароль
LOGIN_PASSWORD = (By.XPATH, "//input[@name='Пароль']")

# кнопка Войти
LOGIN_BUTTON = (By.XPATH, "//Button[text()='Войти']")

# Всплывающее окно с деталями заказа
WINDOW_WITH_INFO = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")

# Выполнено за всё время
COUNTER_ALL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

# Выполнено за сегодня
COUNTER_TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

# Поле с номером заказа из раздела В работе
ORDER_IN_WORK = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li.text_type_digits-default")