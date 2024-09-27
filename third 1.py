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

    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------


    # Lets say eii website ta te jokhon dhuktesi tokhon ekta pop-up ashtese (Image is given in the folder. file is "image.png")
    # Ekhane no thanks e click korle then further procced korbe. Otherwise korbe na. 
    # So emon kisu korte hobe jeno selenium No Thanks e tap kore
    # Ora j website ta use korse oita currently exist kore na. So here it just given the sample of code!! :)



    # Ekhon ekhetre try and except use korte hobe. Karon joruri na j shob shomoii e eii pop up ta ashbe
    # Jodi pop-up ta porobortite na pay tahole to abar code run korte fail korbe

# try:
    
#     no_button = driver.find_element(By.CLASS_NAME, 'at-cm-button')
#     no_button.click()

# except:

#     print("No element with this class name. Skipping")






    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------


    # Ager motoii ID diye name nd email specify kore diche

name = driver.find_element(By.ID, "name")
email = driver.find_element(By.ID, "email")


    # Name nd email ta pathay ditesi key akare. O eta diye fill up kore dibe form ta
    
name.send_keys("Leonardo De Caprio")
email.send_keys("leocap@xyz.com")