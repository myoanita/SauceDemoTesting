class LoginPage ():
    def __init__(self,driver):
        self.driver = driver
        self.username_text_box_id = "user-name"
        self.password_text_box_id = "password"
        self.login_button_id = "login-button"
        self.error_message_tag = "h3"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_text_box_id).clear()
        self.driver.find_element_by_id(self.username_text_box_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_text_box_id).clear()
        self.driver.find_element_by_id(self.password_text_box_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def error_message(self):
        error = self.driver.find_element_by_tag_name(self.error_message_tag).text
        return error