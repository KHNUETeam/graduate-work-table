from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import MySQLdb

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://irbis-nbuv.gov.ua/cgi-bin/irbis64r_81/cgiirbis_64.exe?C21COM=F&I21DBN=ARD_EX&P21DBN=ARD&S21FMT=&S21ALL=&Z21ID=')
time.sleep(5)

element = Select(driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(5) > td.main_content > table > tbody > tr > td > table > tbody > tr:nth-child(6) > td:nth-child(2) > select'))
element.select_by_value('У$')

element = driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(5) > td.main_content > table > tbody > tr > td > table > tbody > tr:nth-child(12) > td > input[type="submit"]:nth-child(2)')
element.click()

time.sleep(3)

element = driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(5) > td.main_content > table:nth-child(5) > tbody > tr:nth-child(4) > td:nth-child(2) > font > table > tbody > tr > input[type="hidden"]:nth-child(103)')
count = int(element.get_attribute('value'))

#start on 8
author_selector = 'body > table > tbody > tr:nth-child(5) > td.main_content > table:nth-child(5) > tbody > tr:nth-child({}) > td:nth-child(2) > a'
theme_selector = 'body > table > tbody > tr:nth-child(5) > td.main_content > table:nth-child(5) > tbody > tr:nth-child({}) > td:nth-child(2) > b:nth-child(5)'

connection = MySQLdb.connect(
    host="localhost",    # your host, usually localhost
    user="topicthesisuser",         # your username
    passwd="uTBzTrkuLnDl",  # your password
    db="topicthesisdb",
    charset='utf8'
)

page = 1
while page < count:
    page += 20
    i = 8
    while True:
        try:
            author = driver.find_element_by_css_selector(author_selector.format(i)).text
            theme = driver.find_element_by_css_selector(theme_selector.format(i)).text

            try:
                cursor = connection.cursor()
                cursor.execute('SELECT * from vern_lib WHERE theme = \'{}\''.format(theme))

                if len(cursor.fetchall()) == 0:
                    cursor.close()
                    cursor = connection.cursor()
                    cursor.execute('INSERT INTO `vern_lib` (`theme`, `author`) VALUES (\'{0}\',\'{1}\')'.format(theme, author))
                    connection.commit()
                    cursor.close()
            except:
                pass

            i += 4
        except:
            page_href = driver.find_element_by_css_selector('#anchor[value="{}"]'.format(page))
            page_href.click()
            break
