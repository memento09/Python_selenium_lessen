from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, requests
import pandas as pd

browser = webdriver.Chrome()
titles = []
evals = []
categories = []
start = time.time()
page = 0

# 全ページの情報を取得
while True:
  page += 1
  url = 'https://scraping-for-beginner.herokuapp.com/ranking/?page={}'.format(page)
  # HTTP ERRORなら処理を中止
  res = requests.get(url)
  res.raise_for_status()

  browser.get(url)

  # 1ページ中の全ての観光地の情報を取得
  elems_rankingbox = browser.find_elements_by_class_name('u_areaListRankingBox')

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

  # CSVに表出力
  df = pd.DataFrame()
  df['観光地名'] = titles
  df['総合評価'] = evals
  df_categories = pd.DataFrame(categories)
  df_categories.columns = ['楽しさ','人混みの多さ','景色','アクセス']
  df = pd.concat([df,df_categories], axis=1)
  df.to_csv('観光地情報.csv', index=False)

  # 次のページがなければ終了
  elem_nextpage = browser.find_element_by_id('pagination')
  try :
    elem_disable = elem_nextpage.find_element_by_class_name('disabled')
  except NoSuchElementException:
    pass
  else:
    elem_disable = elem_nextpage.find_element_by_class_name('disabled')
    elem_next = elem_disable.text
    if elem_next == 'chevron_right':
      break
    time.sleep(3)

print('finish!')
browser.close
browser.quit