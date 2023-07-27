from selenium.webdriver.common.by import By



class All_locators:

    SIG_IN_BUTTON = (By.XPATH, '//button[@id = "passp:sign-in"]')
    EMAIL_FIELD = (By.XPATH, '//input[@id = "passp-field-login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id = "passp-field-passwd"]')
    CHANGE_ACCOUNT_BUTTON = (By.XPATH, '//span[@class = "AddAccountButton-icon"]')
    EMAIL_FIELD_HINT = (By.XPATH, '//div[@id ="field:input-login:hint"]')
    PASSWORD_FIELD_HINT = (By.XPATH, '//div[@id ="field:input-passwd:hint"]')

