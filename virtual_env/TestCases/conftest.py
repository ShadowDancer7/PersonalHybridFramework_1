import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    baseURL = "https://www.opencart.com/index.php?route=common/home"
    
    if browser == "chrome":
        driver = webdriver.Chrome("C:\\Users\\Shado\\Documents\\ChromeDriver_3\\chromedriver.exe")
        driver.get(baseURL)
    elif browser == "internet_explorer":
        driver = webdriver.Ie("C:\\Users\\Shado\\Documents\\InternetExplorerDriver\\IEDriverServer.exe")
        driver.get(baseURL)
    elif browser == "firefox":
        driver = webdriver.Firefox("C:\\Users\\Shado\\Documents\\Firefox_GeckoDriver\\geckodriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############## Adding HTML Report #####################


############## Adding Environment #####################
def pytest_configure(config):
    config._metadata['Project Name'] = 'Open Cart'
    config._metadata['Module Name'] = 'Resource Drop Down Menu'
    config._metadata['Tester'] = 'Benjamin'


############## Delete/modify environment info to HTML report ###################
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)