import locators.orders_feed_page_locators
from page_objects.base_page import BasePageBurger
import allure
import data


class OrderFeedPageBurger(BasePageBurger):

    @allure.step('Ввод email в качестве логина пользователя на странице авторизации')
    def input_email(self):
        input_email = self.wait_and_find_element(locators.orders_feed_page_locators.LOGIN_EMAIL)
        input_email.send_keys(data.Credentials.email)

    @allure.step('Ввод пароля пользователя на странице авторизации')
    def input_password(self):
        input_password = self.wait_and_find_element(locators.orders_feed_page_locators.LOGIN_PASSWORD)
        input_password.send_keys(data.Credentials.password)

    @allure.step('Клик на кнопку "Войти" на странице авторизации')
    def click_login_submit_button(self):
        login_submit_button = self.wait_and_find_element(locators.orders_feed_page_locators.LOGIN_BUTTON)
        login_submit_button.click()

    @allure.step('Получение значения счетчика "Выполнено за всё время"')
    def get_counter_all_orders(self):
        counter = self.wait_and_find_element(locators.orders_feed_page_locators.COUNTER_ALL_ORDERS)
        return int(counter.text)

    @allure.step('Получение значения счетчика "Выполнено за сегодня"')
    def get_counter_today_orders(self):
        counter = self.wait_and_find_element(locators.orders_feed_page_locators.COUNTER_TODAY_ORDERS)
        return int(counter.text)

    @allure.step('Получение номера заказа из раздела В работе')
    def get_number_of_order_in_work(self):
        order_num = self.wait_and_find_element(locators.orders_feed_page_locators.ORDER_IN_WORK)
        return int(order_num.text[1:])
