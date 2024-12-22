import pytest
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage

# Read data from Excel
def get_login_data(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    login_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        login_data.append(row)
    return login_data

# Fixture for WebDriver setup and teardown
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    yield
    driver.quit()

# Test class for data-driven testing
@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.parametrize("username,password", get_login_data("login_data.xlsx"))
    def test_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login()

        if username == "Admin" and password == "admin123":
            assert "dashboard" in self.driver.current_url, "Login failed for valid credentials"
        else:
            error_message = login_page.get_error_message()
            assert "Invalid credentials" in error_message, "Error message not displayed for invalid credentials"

# Generate HTML report
def pytest_html_report_title(report):
    report.title = "Login Automation Test Report"
