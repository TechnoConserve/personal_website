from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options


class BlogPageTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        options = Options()
        options.headless = True
        cls.selenium = WebDriver(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get("{}{}".format(self.live_server_url, "/login/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("test_admin")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("password")

        self.selenium.find_element_by_xpath("/html/body/div/div[2]/form/button[contains(text(), 'Log in')]").click()
