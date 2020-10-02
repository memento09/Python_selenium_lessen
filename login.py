from typing import Text, ValuesView
from selenium import webdriver
import pandas as pd
import time

browser =  webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username = browser.find_element_by_id('username')
elem_password = browser.find_element_by_id('password')
elem_username.send_keys('imanishi')
elem_password.send_keys('kohei')

elem_login = browser.find_element_by_id('login-btn')
elem_login.click()
time.sleep(2)

# テーブルデータを取得する場合
elems_th = browser.find_elements_by_tag_name('th')
key = elems_th[0].text

keys = []

for elem_th in elems_th:
  key = elem_th.text
  keys.append(key)

print(keys)

values = []

elems_td = browser.find_elements_by_tag_name('td')
value = elems_td[0].text

for elem_td in elems_td:
  value = elem_td.text
  values.append(value)

print(values)

# CSVファイルに出力
# 空のDataFrameを定義
df = pd.DataFrame()

df['項目'] = keys
df['値'] = values
df.to_csv('講師情報.csv',index=False)

# 一つずつ取得する場合
# elem_name = browser.find_element_by_id('name')
# elem_company = browser.find_element_by_id('company')
# elem_birthday = browser.find_element_by_id('birthday')
# elem_home = browser.find_element_by_id('come_from')
# elem_hobby = browser.find_element_by_id('hobby')

# print(f'講師名： {elem_name.text}')
# print(f'所属企業： {elem_company.text}')
# print(f'生年月日： {elem_birthday.text}')
# print(f'出身： {elem_home.text}')
# print(f'趣味： {elem_hobby.text}')

browser.quit
