from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import time
import sys

# Use https://www.proxynova.com/proxy-server-list/country-tr/ to find a good proxy to use
PROXY = "209.126.4.134:3128"

chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

# Install chromedriver and change PATH as required
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

search_item = "lamp"

url = "https://www.letgo.com/en-tr/c/all?searchTerm=" + search_item
driver.get(url)

try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.TAG_NAME, "h1")))
finally:
    pass

while True:
    try:
        driver.find_element_by_xpath("//span[text()='OOPS! NO RESULTS NEAR YOU']")
    except NoSuchElementException:
        break
    driver.refresh()

title = driver.find_element_by_tag_name("h1").text
number = int(title.split(' ')[0].strip())
print('Number = ' + str(number))

page = number//36
if number % 36 != 0:
    page += 1


while True:
    try:
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, "//a[@data-test='load-more-feed-button']")))
        except:
            break
        #load_more = driver.find_element_by_xpath("//a[@data-test='load-more-feed-button']")
        load_more = driver.find_element_by_xpath("//div[@class='Spacer__SpacerStyled-sc-11kae1j-0 fJddrM Boxstyle__BoxStyled-h0e1j3-0 cTGzaf']")
        load_more.click()
    finally:
        pass

# new_url = 'https://www.letgo.com/en-tr/c/all/page/' + str(page) + '?searchTerm=' + search_item
# driver.get(new_url)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

items = driver.find_elements_by_xpath("//div[@data-testid='feed-grid-item']")
#print(len(items))

final = []

for item in items:
    title = item.find_element_by_xpath("//p[@data-testid='feed-grid-item-name']")
    link = title.find_element_by_tag_name('a').get_attribute('href')
    price = item.find_element_by_xpath("//p[@data-testid='feed-grid-item-price']").text
    final.append([title.text,link,price])

print(final)
