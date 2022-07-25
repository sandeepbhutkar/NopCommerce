from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pageObjects.registrationPage import registrationPage
from utilities import xlUtils
from selenium.webdriver.chrome.options import Options



class Test_registraion:
    #options = Options()
    #options.headless = True

    url = "http://demowebshop.tricentis.com/register"
    # firstname = "firstname"
    # lastname = "lastname"
    # email = "email@email.com"
    # password = "password"
    # confirmpassword = "confirmpassword"
    path = "C:/Users/sbhutkar/PycharmProjects/DemoWebShop/testData/testData.xlsx"
    row = xlUtils.get_row_count(path,"Sheet1")

    def test_register_customer(self):
        for r in range(2, self.row+1):
            self.driver = webdriver.Chrome(executable_path="C:/Users/sbhutkar/Downloads/chromedriver.exe")
            self.driver.get(self.url)
            self.rp = registrationPage(self.driver)
            self.rp.enter_firstname(xlUtils.read_data(self.path, "Sheet1", r, 2))
            self.rp.enter_lastname(xlUtils.read_data(self.path, "Sheet1", r, 3))
            self.rp.enter_email(xlUtils.read_data(self.path, "Sheet1", r, 4))
            self.rp.enter_password(xlUtils.read_data(self.path, "Sheet1", r, 5))
            self.rp.enter_confirmpassword(xlUtils.read_data(self.path, "Sheet1", r, 6))
            self.var1 = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Register')]")

            time.sleep(3)
            self.driver.close()

