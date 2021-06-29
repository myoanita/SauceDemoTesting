class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.title_class = "title"
        self.picture_id_1 = "item_4_img_link"
        self.add_to_cart_id = "add-to-cart-sauce-labs-backpack"
        self.shopping_cart_class = "shopping_cart_link"
        self.cart_class = "cart_quantity"
        self.checkout_id = "checkout"
        self.first_name_id = "first-name"
        self.last_name_id = "last-name"
        self.postal_code_id = "postal-code"
        self.continue_id = "continue"
        self.product_name_id = "item_4_title_link"
        self.finish_id = "finish"
        self.complete_tag = "h2"
        self.back_button_class_name = "btn btn_secondary back btn_large inventory_details_back_button"

    def title_homepage(self):
        title = self.driver.find_element_by_class_name(self.title_class).text
        return title

    def detail_product(self):
        self.driver.find_element_by_id(self.picture_id_1).click()

    def add_to_cart(self):
        self.driver.find_element_by_id(self.add_to_cart_id).click()

    def shopping_cart(self):
        self.driver.find_element_by_class_name(self.shopping_cart_class).click()

    def cart_quantity(self):
        quantity = self.driver.find_element_by_class_name(self.cart_class).text
        return quantity

    def checkout_button(self):
        self.driver.find_element_by_id(self.checkout_id).click()

    def first_name(self, first_name):
        self.driver.find_element_by_id(self.first_name_id).clear()
        self.driver.find_element_by_id(self.first_name_id).send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element_by_id(self.last_name_id).clear()
        self.driver.find_element_by_id(self.last_name_id).send_keys(last_name)

    def postal_code(self, postal_code):
        self.driver.find_element_by_id(self.postal_code_id).clear()
        self.driver.find_element_by_id(self.postal_code_id).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element_by_id(self.continue_id).click()

    def checkout_overview(self):
        product = self.driver.find_element_by_id(self.product_name_id).text
        return product

    def finish_checkout(self):
        self.driver.find_element_by_id(self.finish_id).click()

    def complete_checkout(self):
        complete = self.driver.find_element_by_tag_name(self.complete_tag).text
        return complete