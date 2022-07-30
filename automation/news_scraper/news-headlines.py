from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# path where we are placing our executable file.
application_path = os.path.dirname(sys.executable)

now = datetime.now()
# MMDDYYYY
month_day_year = now.strftime("%m%d%Y")

website = "https://www.thesun.co.uk/sports/football/"
path = "D:/python/webScraping/chromedriver.exe"

# Headless mode
options = Options()
options.headless = True

service = Service(executable_path = path)
driver = webdriver.Chrome(service = service, options = options)
driver.get(website)

containers = driver.find_elements(by = "xpath", value = '//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by = "xpath", value = './a/h2').text
    subtitle = container.find_element(by = "xpath", value = './a/p').text
    link = container.find_element(by = "xpath", value = './a').get_attribute('href')
    # print(title, subtitle, link)
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {"title": titles, "subtitle": subtitles, "link": links}
df_headlines = pd.DataFrame(my_dict)


final_path = f"D:/python/webScraping/headline-hl-{month_day_year}.csv" 
df_headlines.to_csv(final_path)

driver.quit()









