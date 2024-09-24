import os

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC




os.environ['PATH'] += "C:/SeleniumDrivers"

    #For not closing the chrome browser

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

    #-----------------------------This is the basic code------------------------------------------------
    #-----------------------------Here starts the real one----------------------------------------------


