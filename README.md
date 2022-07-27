This is a framework that is designed to test the home page for OpenCart.com
The test cases are created to test the menu of the home page.
To execute the test type this command:
    pytest -v -s --html=Reports/report.html (type the name of the test case here) --browser chrome

    Pytest is installed in the virtual environment, and (--html=Reports/report.html) is the command that will generate 
    the report and a path to view the document. Make sure to click on the report.html file and select copy path so you could paste the entire path in the browser.
    The (--browser) command is the command used to execute the event hooks from the conftest.py file to select the browser to use for testing (chrome, internet explorer, or firefox).
       
