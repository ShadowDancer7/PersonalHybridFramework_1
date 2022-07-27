from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class opencartHomePage_DropDownMenu:
    menu_dropdown_resources = "caret"

    menu_dropdown_open_showcase = "Showcase"
    menu_dropdown_open_contact_us = "Contact"
    menu_dropdown_open_opencart_partners = "OpenCart Partners"
    menu_dropdown_open_community_forums = "Community"
    menu_dropdown_open_facebook_community = "Facebook"
    menu_dropdown_open_opencart_documentation = "OpenCart Documentation"
    menu_dropdown_open_opencart_books = "OpenCart Books"
    menu_dropdown_open_github_bug_tracker = "Git"
    menu_dropdown_open_developer = "Develop"


    def __init__(self, driver):
        self.driver = driver

    def click_DropdownMenu_Resources(self):
        WebDriverWait(self.driver, 150000)        
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()

    def clickDropDown_select_Showcase(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.LINK_TEXT, self.menu_dropdown_open_showcase).click()
    
    def clickDropDown_select_ContactUs(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.menu_dropdown_open_contact_us).click()
    
    def clickDropDown_select_OpencartPartners(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.LINK_TEXT, self.menu_dropdown_open_opencart_partners).click()

    def clickDropDown_select_CommunityForums(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.menu_dropdown_open_community_forums).click()
    
    def clickDropDown_select_FacebookCommunity(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.menu_dropdown_open_facebook_community).click()
        

    def clickDropDown_select_OpencartDocumentation(self):
        WebDriverWait(self.driver, 150000)
        
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.LINK_TEXT, self.menu_dropdown_open_opencart_documentation).click()

    def clickDropDown_select_OpencartBooks(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.LINK_TEXT, self.menu_dropdown_open_opencart_books).click()

    def clickDropDown_select_GithubBugTracker(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.menu_dropdown_open_github_bug_tracker).click()
    
    def clickDropDown_select_Developer(self):
        WebDriverWait(self.driver, 150000)
        self.driver.find_element(By.CLASS_NAME, self.menu_dropdown_resources).click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.menu_dropdown_open_developer).click()
    