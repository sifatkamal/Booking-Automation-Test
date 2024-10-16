import os
import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):

    def __init__(self, driver_path = r"C:/SeleniumDrivers"):

        self.driver_path = driver_path

        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)

        super(Booking, self).__init__()

    def land_first_page(self):

        self.get(const.BASE_URL)

