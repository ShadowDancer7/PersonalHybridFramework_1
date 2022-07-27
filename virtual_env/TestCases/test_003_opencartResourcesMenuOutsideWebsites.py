from selenium import webdriver
from PageObject.opencartHomePage_ResourceDropDownMenu import opencartHomePage_DropDownMenu
from Utilities.customLogger import LogGenerator


class Test_HomePage_OutsideWebsites:
    logger = LogGenerator.generateLog()

    def test_HomePageDropDownMenu_CommunityForums(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info("**********Launch Chrome Browser - Testing link to outside website: Community Forums ************")
        self.test_dropdown_menu = opencartHomePage_DropDownMenu(self.driver)
        self.test_dropdown_menu.clickDropDown_select_CommunityForums()
        self.ver_title = self.driver.title
        if self.ver_title == 'OpenCart Community - Index page':
            self.logger.info("********* Verified Opencart title: Community Index passed **************")
            assert True
        else:
            self.logger.info("********* Verified Opencart title: Community Index failed **************")
            self.driver.save_screenshot(".\\Screenshots\\test_004_opencartResourcesMenuOutsideWebsites_CommunityForums.png")
            assert False
        self.driver.close()
    
    def test_HomePageDropDownMenu_FacebookCommunity(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info("**********Launch Chrome Browser - Testing link to outside website: Facebook Community ************")
        self.test_dropdown_menu = opencartHomePage_DropDownMenu(self.driver)
        self.test_dropdown_menu.clickDropDown_select_FacebookCommunity()
        self.ver_title = self.driver.title
        if self.ver_title == 'OpencartDesk | Facebook':
            self.logger.info("********* Verified Opencart title: Facebook passed **************")
            assert True
        else:
            self.logger.info("********* Verified Opencart title: Facebook failed **************")
            self.driver.save_screenshot(".\\Screenshots\\test_004_opencartResourcesMenuOutsideWebsites_FacebookCommunity.png")
            assert False
        self.driver.close()
    
    def test_HomePageDropDownMenu_GithubBugTracker(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info("**********Launch Chrome Browser - Testing link to outside website: Github Bug Tracker ************")
        self.test_dropdown_menu = opencartHomePage_DropDownMenu(self.driver)
        self.test_dropdown_menu.clickDropDown_select_GithubBugTracker()
        self.ver_title = self.driver.title
        if self.ver_title == 'Issues - opencart/opencart':
            self.logger.info("********* Verified Opencart title: Github passed **************")
            assert True
        else:
            self.logger.info("********* Verified Opencart title: Github failed **************")
            self.driver.save_screenshot(".\\Screenshots\\test_004_opencartResourcesMenuOutsideWebsites_GithubBugTracker.png")
            assert False
        self.driver.close()

