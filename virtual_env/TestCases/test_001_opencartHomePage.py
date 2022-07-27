from selenium import webdriver
from PageObject.opencartHomePage import opencartHomePage_Menu
from Utilities.customLogger import LogGenerator

class Test_001_OpenCartHomePage:

    logger = LogGenerator.generateLog()

    def test_opencart_homepage(self, setup):
        self.driver = setup
        self.logger.info("*********** Launch chrome browser - Testing OpenCart Menu************")
        self.opencarthomepage = opencartHomePage_Menu(self.driver)
        self.opencarthomepage.clickMenuFeatures()
        self.driver.implicitly_wait(40)
        self.ver_title_features = self.driver.title
        if self.ver_title_features == 'OpenCart - Features':
            self.logger.info("******** Verified Opencart title: OpenCart Features - passed ****************")
            assert True
        else:
            self.logger.info("******** Verified Opencart title: OpenCart - Features - failed")
            self.driver.save_screenshot(".\\Screenshots\\test_001_opencartHomePage_opencart_features.png")
            assert False

        self.opencarthomepage.clickMenuDemo()
        self.driver.implicitly_wait(40)
        ver_title_demo = self.driver.title
        if ver_title_demo == 'OpenCart - Demo':
            self.logger.info("******** Verified Opencart title: OpenCart Demo - passed ****************")
            assert True
        else:
            self.logger.info("******** Verified Opencart title: OpenCart Demo - failed ****************")
            self.driver.save_screenshot(".\\Screenshots\\test_001_opencartHomePage_opencart_demo.png")
            assert False

        self.opencarthomepage.clickMenuMarketplace()
        self.driver.implicitly_wait(40)
        ver_title_marketplace = self.driver.title
        if ver_title_marketplace == 'OpenCart - Marketplace':
            self.logger.info("******** Verified Opencart title: OpenCart Marketplace - passed ****************")
            assert True
        else:
            self.logger.info("******** Verified Opencart title: OpenCart Marketplace - failed ****************")
            self.driver.save_screenshot(".\\Screenshots\\test_001_opencartHomePage_opencart_marketplace.png")
            assert False

        self.opencarthomepage.clickMenuBlog()
        self.driver.implicitly_wait(40)   
        ver_title_blog = self.driver.title
        if ver_title_blog == 'OpenCart - Blog':
            self.logger.info("******** Verified Opencart title: OpenCart - Blog - passed ****************")
            assert True
        else:
            self.logger.info("******** Verified Opencart title: OpenCart - Blog - failed ****************")
            self.driver.save_screenshot(".\\Screenshots\\test_001_opencartHomePage_opencart_blog_module_free.png")
            assert False

        self.opencarthomepage.clickMenuDownload()
        self.driver.implicitly_wait(40)
        ver_title_download = self.driver.title
        if ver_title_download == 'OpenCart - Downloads':
            self.logger.info("******** Verified Opencart title: OpenCart - Downloads - passed ****************")
            assert True
        else:
            self.logger.info("******** Verified Opencart title: OpenCart Downloads - failed ****************")
            self.driver.save_screenshot(".\\Screenshots\\test_001_opencartHomePage_opencart_downloads.png")
            assert False
        self.driver.close()





