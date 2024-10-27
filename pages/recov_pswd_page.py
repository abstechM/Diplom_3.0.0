import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_recov_pswd import ResetPswdLocators
from pages.base_page import BasePage


class PswdPage(BasePage):
    @allure.step("Ввести email")
    def input_email_for_reset_password(self, email):
        self.set_text_to_elemet(ResetPswdLocators.INPUT_EMAIL, email)


    @allure.step("Нажать Восстановить")
    def click_recovery_button(self):
        self.click_on_element(ResetPswdLocators.BUTTON_RESET)

    @allure.step("Нажать показать Пароль")
    def click_show_pswd(self):
        self.click_on_element(ResetPswdLocators.BUTTON_SHOW)

    def find_active_field(self):
        return self.find_element_with_wait(ResetPswdLocators.ACTIVE_FILED)