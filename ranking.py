from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

# １つの観光地情報を取得
elem_rankingbox = browser.find_element_by_class_name('u_areaListRankingBox')
elem_title = elem_rankingbox.find_element_by_class_name('u_title')
elem_eval = browser.find_element_by_class_name('u_rankBox')
elem_eval = elem_eval.find_element_by_class_name('evaluateNumber')
elem_rank = browser.find_element_by_class_name('u_categoryTipsItem')
elem_fun = elem_rank.find_elements_by_class_name('is_rank')[0]
elem_cloud = elem_rank.find_elements_by_class_name('is_rank')[1]
elem_scape = elem_rank.find_elements_by_class_name('is_rank')[2]
elem_access = elem_rank.find_elements_by_class_name('is_rank')[3]

txt_title = elem_title.text
txt_eval = elem_eval.text
txt_fun = elem_fun.text

print(txt_title.split('\n')[1])
print(txt_eval)

browser.quit