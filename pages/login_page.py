import allure
from locators.locators_login_page import LogLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Ввод email")
    def input_email(self, email):
        self.set_text_to_elemet(LogLocators.EMAIL_INPUT, email)

    @allure.step("Ввод пароль")
    def input_pswd(self, password):
        self.set_text_to_elemet(LogLocators.PSWD_INPUT, password)

    @allure.step("Нажать на кнопку Войти")
    def click_enter_button(self):
        self.click_on_element(LogLocators.ENTER_BUTTON)

    @allure.step("Нажать на Восстановить пароль")
    def click_reset_password_button(self):
        self.click_on_element(LogLocators.FORGOT_BUTTON)


    def login(self, email, password):
        self.input_email(email)
        self.input_pswd(password)
        self.click_enter_button()
