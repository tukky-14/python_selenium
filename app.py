from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Chromeドライバーを起動
driver = webdriver.Chrome()

# Googleのホームページにアクセス
driver.get("http://www.google.com")

# 検索ボックスに入力
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Hello, Selenium!")

# 検索を実行
search_box.send_keys(Keys.RETURN)

# 結果が表示されるまで大輝
time.sleep(1)

# 検索結果のURLを取得
search_results = driver.find_element(By.ID, "rso").find_elements(By.TAG_NAME, "a")
for result in search_results:
    title = result.find_element(By.TAG_NAME, "h3")
    url = result.get_attribute('href')
    print(title.text)
    print(url)

# ブラウザを閉じる
driver.quit()