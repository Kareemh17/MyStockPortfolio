from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader as web

driver = webdriver.Chrome()
driver.get('https://robinhood.com/login')
user = driver.find_element_by_name('username')
user.send_keys('##################') # place username here
password = driver.find_element_by_name('password')
password.send_keys('################') # place password here
driver.find_element_by_class_name('_1q0oQo76jB7KFKWPCMPzDW').click()
time.sleep(10)

# web-scraping
html = driver.page_source
htmlsource = soup(html, 'html.parser')
for htmlbody in htmlsource.find_all('body', {'class': 'theme-closed-up market-closed'}):
    for section in htmlbody.find_all('section', {'class': 'YLFjqZadf9w1jyeOvaT08'}):
        with open('body.txt', 'w') as infile:
            for line in htmlbody:
                infile.write(str(line))


style.use("ggplot")
start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()
df = web.get_data_yahoo('BOTZ', dt.datetime(2019, 1, 31), end)
df1 = web.get_data_yahoo('AIQ', dt.datetime(2019, 2, 5), end)
df2 = web.get_data_yahoo('BLRX', dt.datetime(2019, 2, 5), end)
df3 = web.get_data_yahoo('UCO', dt.datetime(2019, 1, 30), end)
df4 = web.get_data_yahoo('KTOS', dt.datetime(2019, 2, 5), end)
df5 = web.get_data_yahoo('SPY', dt.datetime(2019, 2, 1), end)

adj = (df['Adj Close'] - df['Adj Close'][0]) * 5
adj1 = (df1['Adj Close'] - df1['Adj Close'][0]) * 4
adj2 = (df2['Adj Close'] - df2['Adj Close'][0]) * 100
adj3 = (df3['Adj Close'] - df3['Adj Close'][0]) * 6
adj4 = (df4['Adj Close'] - df4['Adj Close'][0]) * 5
adj5 = df5['Adj Close'] - df5['Adj Close'][0]
total = adj + adj1 + adj2 + adj3 + adj4 + adj5
with plt.style.context('seaborn-bright'):
    total.plot(label='Total Portfolio Assets', c='B')
    adj.plot(label='BOTZ')
    adj1.plot(label='AIQ')
    adj2.plot(label='BLRX')
    adj3.plot(label='UCO')
    adj4.plot(label='KTOS')
    adj5.plot(label='S&P 500')
    plt.xlabel('Time')
    plt.ylabel('Profit')
    plt.legend()
    plt.show()
