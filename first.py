import os

from selenium import webdriver

from selenium.webdriver.common.by import By

os.environ['PATH'] += "C:/SeleniumDrivers"

    #For not closing the chrome browser

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

    #-----------------------------This is the basic code------------------------------------------------
    #-----------------------------Here starts the real one----------------------------------------------


    # Eii website diye amra automation test korbo. Eii website ta te ekta download button Aase
    # Ekhane download button ta manually click korte hobe na. Eii kaj selenium e kore dibe. Amra etaii basically ekhane dekhtesi

    #Website jeta amra use kortesi
    
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")


    # Website mention korsi. Ekhon obiously selenium jane na kishe click korte hobe. So oke specify kore dite hobe.
    # Button er inspect e gele id show korbe button. 
    # Oii id diya ekdom specifically bolar lagbe j eii j eii purticular button ta tumi click korba!!


my_element = driver.find_element(By.ID, "downloadButton")

my_element.click()