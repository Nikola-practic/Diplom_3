from selenium.webdriver.common.by import By

# кнопка "Личный кабинет"
LK_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

# кнопка "Лента Заказов"
ORDER_FEED_BUTTON = (By.XPATH,  "//p[text()='Лента Заказов']")

# кнопка "Оформить заказ"
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

# главный заголовок главной страницы
TITLE = (By.XPATH, "//h1")

# Кнопка Конструктор
CONSTRUCT_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

# Ингредиенты
INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")

# счетчик ингредиента
INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

# корзина-конструктор заказа
CONSTRUCTOR_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")

# заголовок окна с деталями ингредиента
WINDOW_WITH_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")

# кнопка закрыть детали заказа
WINDOW_WITH_DETAILS_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button")

# заголовок в окне оформленного заказа
WINDOW_ORDER_TITLE = (By.XPATH, "//p[text()='идентификатор заказа']")

# окно номера заказа
WINDOW_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")

# кнопка закрыть окно заказа
WINDOW_ORDER_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")