from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://economics.indiana.edu/about/faculty/index.html"
driver.get(url)

print('test')
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CLASS_NAME, "layout")))
finally:
    pass
print('test')

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
faculty_list = driver.find_elements_by_class_name('content')
profs = []

print(len(faculty_list))

with open('./prof-scraper/indiana_cse.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name','designation','email','phone'])
    for faculty in faculty_list:
        # try:
        #     a = faculty.find_elements_by_tag_name('a')[0].get_attribute('href')
        # except:
        #     continue
        # if a not in profs:
        #     profs.append(a)
        #     writer.writerow([a + ","])

        # driver.get(faculty)
        # try:
        #     WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        #         (By.TAG_NAME, "h1")))
        # except:
        #     continue
        # finally:
        #     pass

        try:
            name = faculty.find_elements_by_tag_name('h1')[0].text.replace('\n', ';')
        except:
            continue
        try:
            job = faculty.find_elements_by_class_name('title')[0].text.replace('\n', ';')
        except:
            job = ''
        phone = ''
        email = ''
        a_tag = faculty.find_elements_by_tag_name('a')
        phone = ''
        email = ''
        try:
            for a in a_tag:
                if 'mailto' in a.get_attribute('href'):
                    email = a.get_attribute('href')[7:]
                if 'tel' in a.get_attribute('href'):
                    phone = a.get_attribute('href')[4:]
        except:
            pass
        try:
            writer.writerow([name,job,email,phone])
        except:
            pass

        # deets = driver.find_elements_by_class_name('person--contact')[0].find_elements_by_tag_name('a')
        # email = ''
        # phone = ''
        # for deet in deets:
        #     a = deet.get_attribute('href')
        #     if 'tel' in a:
        #         phone = a[4:]
        #     if 'mailto' in a:
        #         email = a[7:]
        
        # try:
        #     email = faculty.find_elements_by_class_name('action--email')[0].text
        # except:
        #     email = ''
        # try:
        #     phone = faculty.find_elements_by_class_name('faculty-contact__item')[0].text.replace('\n',' ')
        # except:
        #     phone = ''

        # try:
        #     email = deets2.find_elements_by_tag_name('a')[0].get_attribute('href')[7:]
        # except:
        #     pass
        # try:
        #     texts = deets2.text.split('\n')
        #     for text in texts:
        #         if '-' in text:
        #             phone = text
        # except:
        #     pass
            # try:
            #     phone = ''
            # except:
            #     phone = ''
            # try:
            #     email = faculty.find_elements_by_class_name('field-person-email')[0].find_elements_by_tag_name('a')[0].get_attribute('href')[7:]
            # except:
            #     email = ''
        # try:
        # except:
            # continue


print(profs)
driver.quit()