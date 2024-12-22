from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://erail.in/"

        # Locators
        self.from_station_input = (By.ID, "txtStationFrom")
        self.to_station_input = (By.ID, "txtStationTo")
        self.date_picker = (By.ID, "txtJourneyDate")
        self.search_button = (By.ID, "buttonFromTo")
        self.sort_on_date = (By.ID, "chkSelectDateOnly")

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def click_from_station(self):
        from_station_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_station_input)
        )
        from_station_element.click()

    def clear_from_station(self):
        from_station_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_station_input)
        )
        from_station_element.clear()

    def set_from_station(self, from_station):
        from_station_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_station_input)
        )
        from_station_element.send_keys(from_station)

    def select_4th_station(self):
        xpath_4th_station = "(//div[@id='divAutoComplete']/a)[4]"
        fourth_station_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath_4th_station)))
        station_name = fourth_station_element.text
        fourth_station_element.click()
        return station_name

    def set_date(self, journey_date):
        date_picker_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.date_picker)
        )
        date_picker_element.clear()
        date_picker_element.send_keys(journey_date)

    def select_sort_on_date(self):
        sort_on_date_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sort_on_date)
        )
        sort_on_date_element.click()

    def get_dropdown_data(self):  # Wait until the dropdown items are visible
        WebDriverWait(self.driver, 10).until( EC.visibility_of_all_elements_located(self.dropdown_items) ) # Get the text of each dropdown item
        dropdown_elements = self.driver.find_elements(*self.dropdown_items)
        dropdown_data = [element.text for element in dropdown_elements]
        return dropdown_data