from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chromeドライバーを起動
driver = webdriver.Chrome()

# Googleのホームページにアクセス
driver.get("http://www.google.com")

# 検索ボックスに入力
search_box = driver.find_element(by=webdriver.common.by.By.NAME, value="q")
search_box.send_keys("Hello, Selenium!")

# 検索を実行
search_box.send_keys(Keys.RETURN)

# 結果が表示されるまで大輝
time.sleep(5)

# ブラウザを閉じる
driver.quit()