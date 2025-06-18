import allure
from page_objects.home_page import HomePageBurger


class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_construct_button_redirect(self, driver):
        home_page = HomePageBurger(driver)

        # Клик на кнопку "Лента Заказов" вверху главной страницы
        home_page.click_order_feed_button()

        # Клик на кнопку "Конструктор" в левом верхнем углу страницы Лента заказов
        home_page.click_construct_button()

        # Проверка, что текущая страница это главная страница
        home_page.check_current_url()

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_order_feed_button_redirect(self, driver):
        home_page = HomePageBurger(driver)

        # Клик на кнопку "Лента Заказов" вверху главной страницы
        home_page.click_order_feed_button()

        # Проверка, что текущая страница это страница Ленты заказов'
        home_page.check_order_url()

    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_click_ingredient_window_is_appear(self, driver):
        home_page = HomePageBurger(driver)

        # Клик на ингредиент в разделе Конструктор на главной странице
        home_page.click_ingredient()

        # Проверка, что всплывающее окно с деталями ингредиента появляется
        home_page.check_window_with_ingredient_detail_is_appear()

    @allure.title('Проверка закрытия всплывающего окна с деталями при клике по крестику ')
    def test_close_window_with_detail(self, driver):
        home_page = HomePageBurger(driver)
        # Клик на ингредиент в разделе Конструктор на главной странице
        home_page.click_ingredient()

       # Клик на кнопку закрытия всплывающего окна с деталями ингредиента
        home_page.click_window_with_detail_close_button()

        # Проверка, что всплывающее окно с деталями ингредиента закрывается
        home_page.check_window_with_ingredient_detail_is_disappear()

    @allure.title('Проверка увеличения показателя счетчика ингредиента после добавлении ингредиента в заказ')
    def test_add_ingredient_in_order_counter_is_increased(self, driver):
        home_page = HomePageBurger(driver)

        # Перемещение ингредиента в корзину-конструктор
        home_page.move_ingredient_to_order()

        # Проверка увеличения показателя счетчика ингредиента после добавления его в корзину-конструктор
        home_page.check_ingredient_counter_is_increased()

