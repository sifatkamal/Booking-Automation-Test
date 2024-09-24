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


    # Eii website diye amra automation test korbo. Eii website ta te ekta download button Aase
    # Ekhane download button ta manually click na korte hobe na. Eii kaj selenium e kore dibe. Amra etaii basically ekhane dekhtesi

    #Website jeta amra use kortesi
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")


    # Website mention korsi. Ekhon obiously selenium jane na kishe click korte hobe. So oke specify kore dite hobe.
    # Button er inspect e gele id show korbe button. 
    # Oii id diya ekdom specifically bolar lagbe j eii j eii purticular button (downloadButton) ta tumi click korba!!

    # Implicit wait: driver.implicit_wait(30) eta dile o jeta korbe 30 seconds porjonto wait korbe website ta properly load howar jonno
    # Erokom na j o 30 seconds porjontoii wait korbe. Jodi website load hoye jay eii 30 seconds er modhe then o r 30 seconds porjonto hudaii
    # wait kobe na
    # Ekhane time.sleep(30) o use kora jaito. Bt o tokhon 30 second porjonto hold kore boshe thakto

driver.implicitly_wait(30)

my_element = driver.find_element(By.ID, "downloadButton")

my_element.click()


    # J text ta show korbe oita show korbe

# ---------------------------Codes-------------------------------------

    # Ekhane eta dile thik motoii kaj kore. bt kisu issues ase
    # Jokhon eta dibo jeii text taii o shuru te pache oitaii diye dibe
    # Ekhon etar jonno explicit wait use kora jaite pare. O jeta korbe ekta nirdishto time porjonto wait kobe 
    # until conditions are not fully matched within the time diration

# progress_element = driver.find_element(By.CLASS_NAME, "progress-label")

# print(f"{progress_element.text == 'Completed!'}")

# ---------------------------Codes-------------------------------------


    #Eta make sure kortese. Download ta complete hobe then code ta shesh hobe

    # Ekhane basically 30s wait kortese condition met howar jonnno. Jodi hoye jay then o r wait korbe na 30s. Further agabe

    # .until jeta ase oita bujhache 30 wait korbe until nicher code ta execution shesh hoche

    # Ekhane progress-label naam e j class ta oita "Complete!" text tar jonno wait kortese. Jokhon e pabe oita code shesh kore dibe

    # Jodi "Complete!" text ta na pay 30s er modhe Timeout Exception show korbe

WebDriverWait(driver, 30).until(

    EC.text_to_be_present_in_element(

        (By.CLASS_NAME, 'progress-label'), # Element filteration

        'Complete!' #The expected text

    )

)