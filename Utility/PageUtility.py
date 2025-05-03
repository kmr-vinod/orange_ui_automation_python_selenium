import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)
logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

DYNAMICLABEL = '~Dynamic-Label~'
#XPATHS
BTN_BY_LABEL_XPATH = "//button[normalize-space()='~Dynamic-Label~']"
TXTFLD_BY_LABEL_XPATH = "//label[text()='~Dynamic-Label~']/parent::*/following-sibling::*//input"
MENU_BY_LABEL_XPATH = "//span[normalize-space()='~Dynamic-Label~']/parent::a"
#CSS_SELCETORS
LOGGEDIN_CSS_SELECTOR = '.oxd-userdropdown-name'

class PageUtility:

    def launchUrl(self, url: str):
        logger.info('launching url: ', url)
        driver.get(url)
        driver.maximize_window()

    def clickButtonwithLabel(self, label: str):
        xPath = self.getXpath(BTN_BY_LABEL_XPATH, label)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, xPath)))
        element = driver.find_element(By.XPATH, xPath)
        logger.info('Clicking button with label "', label, '"')
        element.click()

    def enterTextFieldwithLabel(self, label: str, data: str):
        xPath = self.getXpath(TXTFLD_BY_LABEL_XPATH, label)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, xPath)))
        element = driver.find_element(By.XPATH, xPath)
        logger.info('Entering data in field "', label, '" with data "', data,'"')
        element.send_keys(data)
        
    def getXpath(self, staticXpath: str, label: str):
        xpath = staticXpath.replace(DYNAMICLABEL, label)
        return xpath

    def verifyTextPresence(self, text: str):
        xPath = self.getXpath(TXTFLD_BY_LABEL_XPATH, text)
        try:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, xPath)))
            assert True, 'Text present on the screen'
        except:
            assert False, 'Text is not present on the screen'

    def verify_dashboard(self):
        try:
            wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, LOGGEDIN_CSS_SELECTOR)))
            assert True, 'Dashboard displayed'
        except:
            assert False, 'Dashboard did not load!'

    def clickLinkwithLabel(self, label: str):
        xPath = self.getXpath(MENU_BY_LABEL_XPATH, label)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, xPath)))
        element = driver.find_element(By.XPATH, xPath)
        logger.info('Clicking side nav menu with label "', label, '"')
        element.click()



