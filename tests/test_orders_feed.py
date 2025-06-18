import allure
from page_objects.home_page import HomePageBurger
from page_objects.orders_feed_page import OrderFeedPageBurger


class TestOrdersFeed:

    @allure.title('Проверка, что при создании нового заказ счётчик "Выполнено за всё время" увеличивается')

    def test_check_counter_all_orders_is_increased(self, driver):
        home_page = HomePageBurger(driver)

        # Клик на кнопку "Лента Заказов" вверху главной страницы
        home_page.click_order_feed_button()

        order_feed_page = OrderFeedPageBurger(driver)

        # Получение значения счетчика "Выполнено за всё время"
        order_count = order_feed_page.get_counter_all_orders()

        # Клик на кнопку "Личный кабинет" в правом верхнем углу главной страницы
        home_page.click_lk_button()

        # order_feed_page = LoginPageBurger(driver)

        # Ввод email в качестве логина пользователя на странице авторизации
        order_feed_page.input_email()

        # Ввод пароля пользователя на странице авторизации
        order_feed_page.input_password()

        # Клик на кнопку "Войти" на странице авторизации
        order_feed_page.click_login_submit_button()

        # Ожидание полной загрузки страницы
        home_page.wait_home_page_loading()

        # Перемещение ингредиента в корзину-конструктор
        home_page.move_ingredient_to_order()

        # Клик на кнопку "Оформить заказ"
        home_page.click_order_button()

        # Клик на кнопку закрытия окна оформленного заказа
        home_page.click_window_order_close_button()

        # Клик на кнопку "Лента Заказов" вверху главной страницы
        home_page.click_order_feed_button()

        # Получение нового значения счетчика "Выполнено за всё время"
        new_order_count = order_feed_page.get_counter_all_orders()

        # Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается
        assert new_order_count > order_count


    @allure.title('Проверка, что при создании нового заказ счётчик "Выполнено за сегодня" увеличивается')

    def test_check_counter_all_orders_is_increased(self, driver):
        home_page = HomePageBurger(driver)

        # Клик на кнопку "Лента Заказов" вверху главной страницы
        home_page.click_order_feed_button()

        order_feed_page = OrderFeedPageBurger(driver)

        # Получение значения счетчика "Выполнено за сегодня"
        order_count = order_feed_page.get_counter_today_orders()

        # Клик на кнопку "Личный кабинет" в правом верхнем углу главной страницы
        home_page.click_lk_button()

        # login_page = LoginPageBurger(driver)

        # Ввод email в качестве логина пользователя на странице авторизации
        order_feed_page.input_email()

        # Ввод пароля пользователя на странице авторизации
        order_feed_page.input_password()

        # Клик на кнопку "Войти" на странице авторизации
        order_feed_page.click_login_submit_button()

        # Ожидание полной загрузки страницы
        home_page.wait_home_page_loading()

        # Перемещение ингредиента в корзину-конструктор
        home_page.move_ingredient_to_order()

        # Клик на кнопку "Оформить заказ"
        home_page.click_order_button()

        # Клик на кнопку закрытия окна оформленного заказа
        home_page.click_window_order_close_button()

        # Клик на кнопку "Лента Заказов" вверху главной страницы
        home_page.click_order_feed_button()

        # Получение нового значения счетчика "Выполнено за сегодня"
        new_order_count = order_feed_page.get_counter_today_orders()

        # Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается
        assert new_order_count > order_count



    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_check_order_number_in_order_in_work(self, driver):
        home_page = HomePageBurger(driver)

        # Клик на кнопку "Личный кабинет" в правом верхнем углу главной страницы
        home_page.click_lk_button()

        order_feed_page = OrderFeedPageBurger(driver)

        # Ввод email в качестве логина пользователя на странице авторизации
        order_feed_page.input_email()

        # Ввод пароля пользователя на странице авторизации
        order_feed_page.input_password()

        # Клик на кнопку "Войти" на странице авторизации
        order_feed_page.click_login_submit_button()

        # Ожидание полной загрузки страницы
        home_page.wait_home_page_loading()

        # Перемещение ингредиента в корзину-конструктор
        home_page.move_ingredient_to_order()

        # Клик на кнопку "Оформить заказ"
        home_page.click_order_button()

        # Клик на кнопку закрытия окна оформленного заказа
        home_page.click_window_order_close_button()

        # Клик на кнопку "Лента Заказов" вверху главной страницы
        home_page.click_order_feed_button()

        # Получение номера заказа из раздела "В работе"
        order_num = order_feed_page.get_number_of_order_in_work()

        # Проверка, что после оформления заказа его номер появляется в разделе "В работе"
        assert order_feed_page.get_number_of_order_in_work() == order_num




