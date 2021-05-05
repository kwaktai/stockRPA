import numpy as np
import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# 결과를 저장할 DataFrame
columns = {'Ticker', 'Name', 'Month', 'yr1', 'Expense',
           'Tracking_D', 'Tracking_E_NAV', 'Tracking_E_Index'}
result = pd.DataFrame(columns=columns)

# Crawling 막는 Robot 우회 옵션 등
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('headless')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(time_to_wait=5)
url = 'https: // www.etf.com/etfanalytics/etf-finder'
driver.get(url)

# Performance - 1년 수익률
performance = driver.find_element_by_xpath(
    '//*[@id="accordion__title-4"]/div/span')
driver.execute_script("arguments[0].click();", performance)
performance2 = driver.find_element_by_xpath(
    '//*[@id="accordion__title-46"]/span')
driver.execute_script("arguments[0].click();", performance2)
slider = driver.find_element_by_xpath(
    '//*[@id="accordion__body-46"]/div/div[2]/div/div[4]')
driver.execute_script("arguments[0].scrollIntoView();", slider)
time.sleep(2)
ActionChains(driver).drag_and_drop_by_offset(slider, 80, 0).perform()

# Trading Data - AUM(운용규모)
tradingdata = driver.find_element_by_xpath(
    '//*[@id="accordion__title-5"]/div/span')
driver.execute_script("arguments[0].click();", tradingdata)
aum = driver.find_element_by_xpath('//*[@id="accordion__title-50"]/span')
driver.execute_script("arguments[0].click();", aum)
slider2 = driver.find_element_by_xpath(
    '//*[@id="accordion__body-50"]/div/div[2]/div/div[4]')
driver.execute_script("arguments[0].scrollIntoView();", slider2)
time.sleep(2)
ActionChains(driver).drag_and_drop_by_offset(slider2, 100, 0).perform()

# 종목 100개로 선택
hundred = (driver.find_element_by_xpath('//*[@id="results_display"]/div').
           find_elements_by_class_name('display-page')[3].find_element_by_id('inactiveResult'))
driver.execute_script("arguments[0].click();", hundred)
time.sleep(1)

# Performance view
category = driver.find_element_by_xpath('//*[@id="table-tabs"]/li[2]/span')
driver.execute_script("arguments[0].click();", category)

# 데이터 수집
table = driver.find_element_by_xpath('//*[@id="finderTable"]/tbody')
for index, value in enumerate(table.find_elements_by_tag_name('tr')):
    ticker = value.find_elements_by_tag_name("td")[0].text
    name = value.find_elements_by_tag_name("td")[1].text
    yr1 = value.find_elements_by_tag_name("td")[5].text
    result = result.append(
        {'Ticker': ticker, 'Name': name, 'yr1': yr1}, ignore_index=True)
time.sleep(1)

# 각 종목에 대한 상세 정보
i = 1
for ticker in result['Ticker']:
    site = 'https: // www.etf.com' + ticker
    driver.get(site)

   # 'Ticker', 'Name', 'Month', 'yr1', 'Expense', 'Tracking_D', 'Tracking_E_NAV', 'Tracking_E_Index'
    try:
        expense = driver.find_element_by_xpath(
            '//*[@id="fundPortfolioManData"]/section/div[1]/span').text
    except:
        expense = driver.find_element_by_xpath(
            '//*[@id="fundSummaryData"]/section/div[4]/span').text

    try:
        month = driver.find_element_by_xpath(
            '//*[@id="overview"]/div[1]/div[3]/div[1]/div[2]/div/span[2]').text
    except:
        month = driver.find_element_by_xpath(
            '//*[@id="overview"]/div[1]/div[4]/div[1]/div[2]/div/span[2]').text

    try:
        tracking_d = driver.find_element_by_xpath(
            '//*[@id="fundPortfolioManData"]/section/div[2]/span').text
    except:
        tracking_d = 'N/A'
    try:
        tracking_e_nav = driver.find_element_by_xpath(
            '//*[@id="overview"]/div[1]/div[4]/div[1]/div[2]/div/span[5]').text
        tracking_e_index = driver.find_element_by_xpath(
            '//*[@id="overview"]/div[1]/div[4]/div[1]/div[5]/div/span[5]').text
    except:
        tracking_e_nav = driver.find_element_by_xpath(
            '//*[@id="overview"]/div[1]/div[3]/div[1]/div[2]/div/span[5]').text
        tracking_e_index = driver.find_element_by_xpath(
            '//*[@id="overview"]/div[1]/div[3]/div[1]/div[5]/div/span[5]').text

    result.loc[result.Ticker == ticker, 'Expense'] = expense
    result.loc[result.Ticker == ticker, 'Month'] = month
    result.loc[result.Ticker == ticker, 'Tracking_D'] = tracking_d
    result.loc[result.Ticker == ticker, 'Tracking_E_NAV'] = tracking_e_nav
    result.loc[result.Ticker == ticker, 'Tracking_E_Index'] = tracking_e_index
    print('Done : ' + str(i) + '/' + str(len(result)))
    i += 1
    time.sleep(1)

result = result.reindex(columns=columns)
result.to_csv('./etf_result.csv')
driver.close()
print('Complete')
