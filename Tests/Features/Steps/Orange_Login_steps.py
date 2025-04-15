import logging
from behave import given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Utility.ReadConfig import Configurations
from selenium import webdriver


class OrangeUISteps:
    config = Configurations()
    url = ''
    usrName = ''
    pwd = ''
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    @given("login to application")
    def step_login(self):
        OrangeUISteps.url = OrangeUISteps.config.getURL()
        OrangeUISteps.usrName = OrangeUISteps.config.getUsername()
        OrangeUISteps.pwd = OrangeUISteps.config.getPassword()
        OrangeUISteps.logger.info(OrangeUISteps.url)
        OrangeUISteps.logger.info(OrangeUISteps.usrName)
        OrangeUISteps.logger.info(OrangeUISteps.pwd)
        OrangeUISteps.driver.get(OrangeUISteps.url)
        OrangeUISteps.driver.get(OrangeUISteps.url)
        usrNameXpath = "//label[text()='Username']/parent::*/following-sibling::*//input"
        pwdXpath = "//label[text()='Password']/parent::*/following-sibling::*//input"
        btnLogin = "//button[normalize-space()='Login']"
        OrangeUISteps.wait.until(expected_conditions.presence_of_element_located((By.XPATH, usrNameXpath)))
        OrangeUISteps.driver.find_element(By.XPATH, usrNameXpath).send_keys(OrangeUISteps.usrName)
        OrangeUISteps.wait.until(expected_conditions.presence_of_element_located((By.XPATH, pwdXpath)))
        OrangeUISteps.driver.find_element(By.XPATH, pwdXpath).send_keys(OrangeUISteps.pwd )
        OrangeUISteps.wait.until(expected_conditions.presence_of_element_located((By.XPATH, btnLogin)))
        OrangeUISteps.driver.find_element(By.XPATH, btnLogin).click()
        OrangeUISteps.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.oxd-userdropdown-name')))



