from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

url = "https://www.covid19india.org"
options = webdriver.ChromeOptions()
#options = webdriver.Chrome()
options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome("C:\Program Files\cromdriver\chromedriver.exe",options=options)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

tr_tags = soup.find_all('tr' , class_='state')

result = []
for tr_tag in tr_tags:
    td_tags = tr_tag.find_all('td')
     
    state_data = td_tags[0].find('div', class_='title-chevron')
    state= state_data.find('span', class_='title-icon').text

    total1 = td_tags[1].find('span', class_='total').text
    total2 = td_tags[2].find('span', class_='total').text
    total3 = td_tags[3].find('span', class_='total').text
    total4 = td_tags[4].find('span', class_='total').text

    item = {
        "State" : state,
        "Confirmed": total1,
        "Active": total2,
        "Recovered": total3,
        "Deaths": total4
    }
    result.append(item)

df = pd.DataFrame(result)  
df.to_csv("covid_data.csv", index = False,columns=['State', 'Confirmed', 'Active', 'Recovered','Deaths'])

    


