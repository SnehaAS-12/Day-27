#Take any webpage, Scrape the data and try to insert only the class data and save it in excel

pip install requests
pip install lxml
pip install bs4
import requests
result = requests.get('https://www.worldometers.info/coronavirus/country/india/')
import bs4
soup = bs4.BeautifulSoup(result.text,'lxml')
cases = soup.find_all('div' ,class_= 'maincounter-number')
data = []
for i in cases:
    span = i.find('span')
    data.append(span.string)
print(data)
import pandas as pd
df = pd.DataFrame({"CoronaData": data})
df.index = ['TotalCases', ' Deaths', 'Recovered']
df.to_csv('Corona_Data.csv')
