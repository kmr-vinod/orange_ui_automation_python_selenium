from behave import *
from Utility.ReadConfig import Configurations
from Utility.PageUtility import PageUtility

config = Configurations()
pUtility = PageUtility()

class OrangeUISteps:

    @given('login to application')
    def step_login(self):
        url = config.getURL()
        usrName = config.getUsername()
        pwd = config.getPassword()
        pUtility.launchUrl(url)
        pUtility.enterTextFieldwithLabel('Username', usrName)
        pUtility.enterTextFieldwithLabel('Password', pwd)
        pUtility.clickButtonwithLabel('Login')

    @then('verify if dashboard is displayed')
    def verify_dasboard(self):
        pUtility.verify_dashboard()

    @when('click "{label}" link on side navigation')
    def clickLinkOnSideNav(self, label):
        pUtility.clickLinkwithLabel(label)
