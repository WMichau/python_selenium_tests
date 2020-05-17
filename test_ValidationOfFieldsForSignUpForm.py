import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class ValidationOfFieldsForSignUpForm_Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\Michau\Desktop\chromedriver_win32 (1)\chromedriver.exe')
     
    def test_SignUp(self):
        pageUrl = "https://www.phptravels.net/home"
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        #Navigating To Register Page
        driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div/div[2]/div/ul/li[3]/div/a").click()
        driver.find_element_by_xpath('//*[@id="//header-waypoint-sticky"]/div[1]/div/div/div[2]/div/ul/li[3]/div/div/div/a[2]').click()
        time.sleep(2)

        #Check If Page is Correct
        Title = driver.title
        self.assertEqual("Register", Title, "Webpage title is not matching")

        SignUp = driver.find_element_by_xpath("//button[(text()=' Sign Up')]")
        SignUp.click()

        Firstname = driver.find_element_by_xpath("//*[@name='firstname']")
        Lastname = driver.find_element_by_xpath("//*[@name='lastname']")
        Phone = driver.find_element_by_xpath("//*[@name='phone']")
        Email = driver.find_element_by_xpath("//*[@name='email']")       
        Password = driver.find_element_by_xpath("//*[@name='password']")
        ConfirmP = driver.find_element_by_xpath("//*[@name='confirmpassword']")

        Inputs = [Firstname, Lastname, Phone, Email, Password, ConfirmP] 

        #Input incorrect credentials
        for input in Inputs:   
            if(input == Email):
                input.send_keys("Aaaa@")
            elif(input == Password or input == ConfirmP):
                input.send_keys("Aaaaaaa")
            else:
                input.send_keys("Aaa")
            
        SignUp.click()
        time.sleep(2)
     
        #js_string = "var element = document.getElementsByClassName('alert alert-danger')[0];element.remove();"
        #driver.execute_script(js_string)
        
        #If incorrect credentials are entered and warning popup doesn't show up test will fail
        self.assertEqual(True, driver.find_element_by_xpath('//*[@id="headersignupform"]/div[2]/div').is_displayed()) 
        
        for input in Inputs:
            input.clear()

        for input in Inputs:   
            if(input == Email):
                input.send_keys("111@11@.com")
            elif(input == Password or input == ConfirmP):
                input.send_keys("111@")
            else:
                input.send_keys("111")

        SignUp.click()
        time.sleep(2)
        self.assertEqual(True, driver.find_element_by_xpath('//*[@id="headersignupform"]/div[2]/div').is_displayed()) 

        for input in Inputs:
            input.clear()

        for input in Inputs:   
            if(input == Email):
                input.send_keys("awiejiaj@gmail.com")
            elif(input == Password or input == ConfirmP):
                input.send_keys("@@@")
            else:
                input.send_keys("@@@")

        SignUp.click()
        time.sleep(2)
        self.assertEqual(True, driver.find_element_by_xpath('//*[@id="headersignupform"]/div[2]/div').is_displayed())

        for input in Inputs:
            input.clear()

        for input in Inputs:   
            if(input == Email):
                input.send_keys("awiejiaj@gmail.com")
            elif(input == Password or input == ConfirmP):
                input.send_keys("!@#$%^&")
            else:
                input.send_keys("abcdefgh")

        SignUp.click()
        time.sleep(2)
        self.assertEqual(True, driver.find_element_by_xpath('//*[@id="headersignupform"]/div[2]/div').is_displayed()) 

        time.sleep(5)

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()