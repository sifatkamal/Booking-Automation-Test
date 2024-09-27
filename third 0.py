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

driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')

driver.implicitly_wait(5)

    # Ager motoii ID diye name nd email specify kore diche

name = driver.find_element(By.ID, "name")
email = driver.find_element(By.ID, "email")


    # Name nd email ta pathay ditesi key akare. O eta diye fill up kore dibe form ta
    
name.send_keys("Leonardo De Caprio")
email.send_keys("leocap@xyz.com")