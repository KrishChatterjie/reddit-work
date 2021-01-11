# Do 'pip install selenium' in your terminal before you run the program
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import smtplib

# Install chromedriver and change PATH as required
# Use the instructions on http://www.automationtestinghub.com/download-chrome-driver/
PATH = "C:\Program Files (x86)\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

# Change this to your email address
# For example, take abc@gmail.com,
username = "abc"
password = "password"
email = username + "@gmail.com"

url = "https://www.albany.edu/registrar/schedule-of-classes-spring.php"
xpaths = ['/html/body/font/b[37]', '/html/body/font/b[85]', '/html/body/font/b[109]', '/html/body/font/b[133]']
flag = False

def send_email():
    content = "APPLY IMMEDIATELY, A SPOT IS FREE!\n" + url
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(username, password)
    server.sendmail(email, email, content)
    server.quit()


while True:
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, "Course_Subject")))
    finally:
        pass

    course_subject = driver.find_element_by_xpath("//input[@id = 'Course_Subject']")
    course_subject.send_keys("CHM")

    catalog_number = driver.find_element_by_xpath("//input[@id = 'Course_Number']")
    catalog_number.send_keys("124")

    submit = driver.find_element_by_xpath('//input[@type = "submit" and @value = "Submit"]')
    submit.click()


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, xpaths[0])))
    finally:
        pass

    for xpath in xpaths:
        available_seats = driver.find_element_by_xpath(xpath).text
        if available_seats != '0':
            send_email()
            flag = True
            break
    
    if flag:
        break

print("Fin.")
