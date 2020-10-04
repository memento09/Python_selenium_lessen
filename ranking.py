from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

# 全ての観光地の情報を取得
elems_rankingbox = browser.find_elements_by_class_name('u_areaListRankingBox')

titles = []
evals = []
categories = []

for elem_rankingbox in elems_rankingbox:
  # 観光地名
  elem_title = elem_rankingbox.find_element_by_class_name('u_title')
  txt_title = elem_title.text.split('\n')[1]
  titles.append(txt_title)
  # 総合評価
  elem_eval = elem_rankingbox.find_element_by_class_name('u_rankBox')
  elem_eval = elem_eval.find_element_by_class_name('evaluateNumber')
  float_eval = float(elem_eval.text)
  evals.append(float_eval)
  # 各評価
  elem = elem_rankingbox.find_element_by_class_name('u_categoryTipsItem')
  elems_rank = elem.find_elements_by_class_name('is_rank')
  _ranks = []
  for elem_rank in elems_rank:
    rank = elem_rank.find_element_by_class_name('evaluateNumber').text
    _ranks.append(rank)
  categories.append(_ranks)

df = pd.DataFrame()
df['観光地名'] = titles
df['総合評価'] = evals
df_categories = pd.DataFrame(categories)
df_categories.columns = ['楽しさ','人混みの多さ','景色','アクセス']
df = pd.concat([df,df_categories], axis=1)
df.to_csv('観光地情報.csv', index=False)

browser.close
browser.quit