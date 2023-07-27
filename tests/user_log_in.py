from constants import URL, USER, MESSAGE
from pages.log_in_page import AuthorizationPage


class TestAuthorization:

    def test_authorization_with_email(self, driver):
        page = AuthorizationPage(driver, URL.get('authorization_page'))
        page.open()
        page.user_authorization(USER.get('email'), USER.get('password'))
        assert driver.title == 'Дзен'

    def test_authorization_with_login(self, driver):
        page = AuthorizationPage(driver, URL.get('authorization_page'))
        page.open()
        page.user_authorization(USER.get('login'), USER.get('password'))
        assert driver.title == 'Дзен'

    def test_error_message_empty_email_field(self, driver):
        page = AuthorizationPage(driver, URL.get('authorization_page'))
        page.open()
        message = page.check_message_empty_email_field()
        assert message == MESSAGE.get('empty_email_field')


    def test_error_message_empty_password_field(self, driver):
        page = AuthorizationPage(driver, URL.get('authorization_page'))
        page.open()
        message = page.check_error_message_password_field(USER.get('login'), '')
        assert message == MESSAGE.get('empty_password_field')


    def test_error_message_wrong_password(self, driver):
        page = AuthorizationPage(driver, URL.get('authorization_page'))
        page.open()
        message = page.check_error_message_password_field(USER.get('login'), USER.get('wrong_password'))
        assert message == MESSAGE.get('wrong_password')


