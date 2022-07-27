from selenium import webdriver
from PageObject.opencartHomePage_ResourceDropDownMenu import opencartHomePage_DropDownMenu
from Utilities.customLogger import LogGenerator


class Test_HomePage_DropDownMenu:
    
    logger = LogGenerator.generateLog()

    def test_HomePageDropDownMenu(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info("****** Launching Chrome browser - Start positive test********")
        self.test_dropdown_menu = opencartHomePage_DropDownMenu(self.driver)
        self.test_dropdown_menu.click_DropdownMenu_Resources()

        self.test_dropdown_menu.clickDropDown_select_Showcase()
        ver_title_showcase = self.driver.title
        if ver_title_showcase == "OpenCart - Showcase":
            assert True
            self.logger.info("********Verified title: OpenCart - Showcase passed **********")
        else:
            self.logger.info("********Verified title: OpenCart - Showcase failed **********")
            self.driver.save_screenshot(".\\Screenshots\\test_opencartResourcesMenuDropDown.png")
            assert False
        

        self.test_dropdown_menu.clickDropDown_select_ContactUs()
        ver_title_contact_us = self.driver.title
        if ver_title_contact_us == "OpenCart - Contact":
            assert True
            self.logger.info("********Verified title: OpenCart - Contact passed **********")

        else:
            
            self.logger.info("********Verified title: OpenCart - Contact failed **********")
            self.driver.save_screenshot(".\\Screenshots\\test_opencartResourcesMenuDropDown.png")
            assert False

        self.test_dropdown_menu.clickDropDown_select_OpencartPartners()
        ver_title_opencart_partners = self.driver.title
        if ver_title_opencart_partners == "OpenCart - Partners":
            assert True
            self.logger.info("********Verified title: OpenCart - Partners passed **********")
        else:
            self.logger.info("********Verified title: OpenCart - Partners failed **********")
            self.driver.save_screenshot(".\\Screenshots\\test_opencartResourcesMenuDropDown.png")
            assert False

        self.test_dropdown_menu.clickDropDown_select_OpencartDocumentation()
        ver_title_opencart_documentation = self.driver.title
        if ver_title_opencart_documentation == "OpenCart Documentation":
            assert True
            self.logger.info("********Verified title: OpenCart Documentation passed **********")
        else:
            self.logger.info("********Verified title: OpenCart Documentation failed **********")
            self.driver.save_screenshot(".\\Screenshots\\test_opencartResourcesMenuDropDown.png")
            assert False

        self.test_dropdown_menu.clickDropDown_select_OpencartBooks()
        ver_title_opencart_books = self.driver.title
        if ver_title_opencart_books == "OpenCart Documentation":
            assert True
            self.logger.info("********Verified title: OpenCart Documentation passed **********")
        else:
            self.logger.info("********Verified title: OpenCart Documentation failed **********")
            self.driver.save_screenshot(".\\Screenshots\\test_opencartResourcesMenuDropDown.png")
            assert False

        self.test_dropdown_menu.clickDropDown_select_Developer()
        ver_title_developer = self.driver.title
        if ver_title_developer == "OpenCart Documentation":
            assert True
            self.logger.info("********Verified title: OpenCart Documentation passed **********")
        else:
            self.logger.info("********Verified title: OpenCart Documentation failed **********")
            self.driver.save_screenshot(".\\Screenshots\\test_opencartResourcesMenuDropDown.png")
            assert False

        self.driver.close()




       


