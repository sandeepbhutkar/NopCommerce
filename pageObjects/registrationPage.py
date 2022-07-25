from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class registrationPage:
    radio_gender_xpath = "//input[@id='gender-male']"
    txt_firstname_xpath = "//input[@class='text-box single-line']"
    txt_lastname_xpath = "//input[@name='LastName']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_confirmpassword_xpath = "//input[@id='ConfirmPassword']"
    btn_register_xpath = "//input[@id='register-button']"

    def __init__(self,driver):
        self.driver = driver

    def select_gender(self):
        self.driver.find_element(By.XPATH, self.radio_gender_xpath).click()
    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)
    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)
    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)
    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)
    def enter_confirmpassword(self,confirmpassword):
        self.driver.find_element(By.XPATH, self.txt_confirmpassword_xpath).send_keys(confirmpassword)
    def click_register(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()





