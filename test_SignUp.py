import unittest
import time
from selenium import webdriver

class SignUp_Test(unittest.TestCase):
    
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

        #Entering Credentials
        driver.find_element_by_xpath("//*[@name='firstname']").send_keys("Frist Name")
        driver.find_element_by_xpath("//*[@name='lastname']").send_keys("Last Name")
        driver.find_element_by_xpath("//*[@name='phone']").send_keys("111 111 111")
        driver.find_element_by_xpath("//*[@name='email']").send_keys("emaill@email.com")
        driver.find_element_by_xpath("//*[@name='password']").send_keys("11111111")
        driver.find_element_by_xpath("//*[@name='confirmpassword']").send_keys("11111111")

        #Clicking SignUp -> Redirect To Account Page
        driver.find_element_by_xpath("//button[(text()=' Sign Up')]").click()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()