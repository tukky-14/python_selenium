from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# スクリーンショットを保存
def screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    with open("screenshot.png", "wb") as file:
        file.write(screenshot)

# ファイルに出力
def output_file(links):
    with open('output.txt', 'w') as file:
        output = '\n'.join(str(item) for item in links)
        file.write(output)

def seach_google():
    # Chromeオプションを作成してヘッドレスモードを有効にする
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Chromeドライバーを起動
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Googleのホームページにアクセス
    driver.get("http://www.google.com")

    # ウィンドウのサイズを指定
    driver.set_window_size(1280, 800)

    # 検索ボックスに入力
    search_box = driver.find_element(by=By.NAME, value="q")
    search_box.send_keys("Selenium Python")

    # 検索を実行
    search_box.send_keys(Keys.RETURN)

    # 結果が表示されるまで待機
    time.sleep(1)

    # 検索結果のURLを取得
    search_results = driver.find_element(By.ID, "rso").find_elements(By.TAG_NAME, "a")

    search_links = []
    for result in search_results:
        try:
            title = result.find_element(By.CLASS_NAME, "LC20lb")
            url = result.get_attribute('href')
            if title.text != "" and url != "":
                search_links.append(title.text)
                search_links.append(url)
                search_links.append("")
        except NoSuchElementException:
            error = 1

    screenshot(driver)
    output_file(search_links)
    
    driver.quit()


seach_google()