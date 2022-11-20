from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()

class pmi_module:
    def pmi_module(self):
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

class Add_Employee(pmi_module):
    def __init__(self,firstName,middleName,lastName,employeeId):
          self.firstName = firstName
          self.middleName = middleName
          self.lastName = lastName
          self.employee Id = employeeId

    def add_employee(self):
        driver.find_element(By.XPATH,"//input[@name="firstName"]").send_keys(self.firstName)
        driver.find_element(By.XPATH,"//input[@name="middleName"]").send_keys(self.middleName)
        driver.find_element(By.XPATH,"//input[@name="lastName"]").send_keys(self.lastName)
        driver.find_element(By.ID,"0324").send_keys(self.employeeId)
        driver.find_element(By.XPATH,"//button[@type="submit"]").click()

class personal_info(pmi_module):

    def __init__(self,employeeFullname,nickName,employeeId, otherId,SSNnumber,SIN number, driver License-no,
                    license Expirydate,nationality,maritalStatus,dateof Birth,gender,militaryService,smoker,bloodType)
             self.employeeFullname= employeeFullname
             self.nickName = nickName
             self.employeeId = employeeId
             self.otherId = otherId
             self.SSNnumber = SSNnumber
             self.SINnumber = SINnumber
             self.driver License-no = driver License-no
             self.license Expirydate = license Expirydate
             self.nationality = nationality
             self.maritalStatus = maritalStatus
             self.dateof Birth = dateof Birth
             self.gender = gender
             self.militaryService = militaryService
             self.smoker = smoker
             self.bloodType = bloodType

    def personal_info(self):

        