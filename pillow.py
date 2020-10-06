from selenium import webdriver
from PIL import Image
from urllib import request
import io

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/image')

# 全ての画像を取得
elems = browser.find_elements_by_class_name('material-placeholder')

for index, elem in enumerate(elems):
  elem = elem.find_element_by_tag_name('img')
  url = elem.get_attribute('src')

  bin_image = io.BytesIO(request.urlopen(url).read())
  img = Image.open(bin_image)
  # img = img.resize(('1024.768'))
  img.save('image/img{}.jpg'.format(index))

# 1枚の画像を取得
# elem = browser.find_element_by_class_name('material-placeholder')
# elem = elem.find_element_by_tag_name('img')
# url = elem.get_attribute('src')

# bin_image = io.BytesIO(request.urlopen(url).read())
# img = Image.open(bin_image)
# img.save('img01.jpg')

# ローカルの画像を開く
# img = Image.open('sample.jpg')
# img.size
# img = img.resize((1024,768))
# img.save('sample_resize.jpg')

browser.close
browser.quit