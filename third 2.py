import os

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys




os.environ['PATH'] += "C:/SeleniumDrivers"

    #For not closing the chrome browser

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

    #-----------------------------This is the basic code------------------------------------------------
    #-----------------------------Here starts the real one----------------------------------------------

driver.get('https://www.tutorialspoint.com/selenium/practice/text-box.php')

driver.implicitly_wait(5)

    # Ager motoii ID diye name nd email specify kore diche

fullname = driver.find_element(By.ID, "fullname")
email = driver.find_element(By.ID, "email")
address = driver.find_element(By.ID, "address")
password = driver.find_element(By.ID, "password")


    # Name nd email ta pathay ditesi key akare. O eta diye fill up kore dibe form ta
    
fullname.send_keys("Leonardo De Caprio")
email.send_keys("leocap@xyz.com")
address.send_keys("221B Baker Street")

    # Keys diye auto keyboard er button diye input neya jay

password.send_keys(Keys.NUMPAD5, Keys.NUMPAD8, Keys.NUMPAD3, Keys.NUMPAD1)


    # On click thakle nicher code ta kaj korbe. Kintu ekhane On Click naii. So ekhetre kaj korbe na.
    # Will try to do it later ......
    
# btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
# btn.click()