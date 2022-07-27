from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait 

class opencartHomePage_Menu:
    menu_link_features = "Features"
    menu_link_demo = "Demo"
    menu_link_marketplace = "Marketplace"
    menu_link_download = "Download"
    menu_link_blog = "Bl"

    def __init__(self, driver):
        self.driver = driver
    
    def clickMenuFeatures(self):
        self.driver.find_element(By.LINK_TEXT, self.menu_link_features).click()

    def clickMenuDemo(self):
        self.driver.find_element(By.LINK_TEXT, self.menu_link_demo).click()

    def clickMenuMarketplace(self):
        self.driver.find_element(By.LINK_TEXT, self.menu_link_marketplace).click()

    def clickMenuDownload(self):
        self.driver.find_element(By.LINK_TEXT, self.menu_link_download).click()

    def clickMenuBlog(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.menu_link_blog).click()


        
        

        
    



    