import os
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking:

    def __init__(self, driver_path = r"C:/SeleniumDrivers", teardown = False):

        self.driver_path = driver_path
        self.teardown = teardown

        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        super(Booking, self).__init__()


        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        if self.teardown == True:
            
            self.driver.quit()

    def land_first_page(self):

        self.driver.get(const.BASE_URL)

        # In the website a popup appears in first page. Removed that popup in the next try except condition

        try:

            # no_button = WebDriverWait(self.driver, 10).until(
            #     self.driver.find_element(By.XPATH, "//*[name() = 'svg' and @xmlns='http://www.w3.org/2000/svg']")    
            # )

            no_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[name() = 'svg' and @xmlns='http://www.w3.org/2000/svg']"))
            )

            no_button.click()
            print("Clicked the cross!! Dont't worry")

        except:

            print("Everything is alright")

    def change_currency(self, currency = None):

        # currency_element = self.driver.find_element(By.CLASS_NAME, f'e4adce92df = "selected_currency={currency}"')

        currency_element = self.driver.find_element(By.CLASS_NAME, 'e4adce92df')
        
        currency_element.send_keys(f'selected_currency={currency}')

        currency_element.click()

        
