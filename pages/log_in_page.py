from selenium.common import TimeoutException

from pages.basepage import BasePage
from locators.log_in_page_locators import All_locators
import time


class AuthorizationPage(BasePage):
    locators = All_locators

    def user_authorization(self, username, password):
        self.username = username
        self.password = password

        try:
            self.element_is_present(self.locators.CHANGE_ACCOUNT_BUTTON).click()
        except TimeoutException:
            pass

        self.element_is_present(self.locators.EMAIL_FIELD).send_keys(self.username)
        self.element_is_clickable(self.locators.SIG_IN_BUTTON).click()
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.password)
        self.element_is_present(self.locators.SIG_IN_BUTTON).click()
        time.sleep(3)

    def check_message_empty_email_field(self):

        try:
            self.element_is_present(self.locators.CHANGE_ACCOUNT_BUTTON).click()
        except TimeoutException:
            pass

        self.element_is_present(self.locators.SIG_IN_BUTTON).click()
        error_message = self.element_is_present(self.locators.EMAIL_FIELD_HINT).text
        return error_message


    def check_error_message_password_field(self, username, password):
        self.username = username
        self.password = password

        try:
            self.element_is_present(self.locators.CHANGE_ACCOUNT_BUTTON).click()
        except TimeoutException:
            pass

        self.element_is_present(self.locators.EMAIL_FIELD).send_keys(self.username)
        self.element_is_clickable(self.locators.SIG_IN_BUTTON).click()
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.password)
        self.element_is_present(self.locators.SIG_IN_BUTTON).click()
        error_message = self.element_is_present(self.locators.PASSWORD_FIELD_HINT).text
        return error_message




