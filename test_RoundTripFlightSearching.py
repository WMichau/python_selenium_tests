import unittest
import time
from selenium import webdriver

class RoundTripFlightSearching_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\Michau\Desktop\chromedriver_win32 (1)\chromedriver.exe')
     
    def test_RoundTripFlightSearchingTest(self):
        pageUrl = "https://www.phptravels.net/home"
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        
        #Click on Flights Tab
        driver.find_element_by_xpath('//*[@id="search"]/div/div/div/div/div/nav/ul/li[2]/a').click()

        #Check RoundTrip Button
        driver.find_element_by_xpath('//*[@id="flights"]/div/div/form/div/div[1]/div[1]/div/div[2]/label').click()

        #Select 'From' Location
        Origin = driver.find_element_by_xpath('//*[@id="s2id_location_from"]/a')
        Origin.click()
        Origin.send_keys("New")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[12]/div/span').click()

        #Select 'To' Location
        Destination = driver.find_element_by_xpath('//*[@id="s2id_location_to"]/a')
        Destination.click()
        Destination.send_keys("Ott")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[23]/div').click()
        
        #Select Class Type
        driver.find_element_by_xpath('//*[@id="flights"]/div/div/form/div/div[1]/div[2]/div/div').click()
        Classes = driver.find_element_by_xpath('//*[@id="flights"]/div/div/form/div/div[1]/div[2]/div/div/div/ul')
        ClassesTypes = Classes.find_elements_by_tag_name("li")
        for item in ClassesTypes:
            if(item.text == 'First'):
                item.click()

        #Pick Dates
        driver.find_element_by_xpath('//*[@id="FlightsDateStart"]').click()
        driver.find_element_by_xpath('//*[@id="datepickers-container"]/div[8]/div/div/div[2]/div[23]').click()
        
        driver.find_element_by_xpath('//*[@id="FlightsDateEnd"]').click()
        driver.find_element_by_xpath('//*[@id="datepickers-container"]/div[9]/div/div/div[2]/div[25]').click()

        #Click on Passanger Amount Buttons
        AdultAdd = driver.find_element_by_xpath('//*[@id="flights"]/div/div/form/div/div[3]/div[3]/div/div/div[1]/div/div[2]/div/span/button[1]')
        AdultSub = driver.find_element_by_xpath('//*[@id="flights"]/div/div/form/div/div[3]/div[3]/div/div/div[1]/div/div[2]/div/span/button[2]')
        ChildAdd = driver.find_element_by_xpath('//*[@id="flights"]/div/div/form/div/div[3]/div[3]/div/div/div[2]/div/div[2]/div/span/button[1]')
        
        for i in range(2):
             AdultAdd.click()
             pass
        AdultSub.click()
        ChildAdd.click()

        #Click Search => Redirect to Flights Page
        driver.find_element_by_xpath('//*[@id="flights"]/div/div/form/div/div[3]/div[4]/button').click()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()