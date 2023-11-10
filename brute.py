from selenium import webdriver
from itertools import product
import string
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import itertools
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool


# 設定 Chrome 瀏覽器的執行檔路徑， r"..." 來指定 ChromeDriver 路徑，這可以確保程式碼中的反斜線（\）被當作字元而非跳脫字元處理。
chrome_driver_path = r"Chrome 瀏覽器的執行檔路徑"

# 啟動 Chrome 瀏覽器(加上路徑和插件的選項)
driver = webdriver.Chrome()
driver.service.executable_path = chrome_driver_path

# 啟動瀏覽器並打開你的網頁
driver.get("輸入欄位的網址")



# 產生所有可能的X位數字及大寫字母組合
chars = string.digits + string.ascii_uppercase
combos = itertools.product(chars, repeat=X)

# 按迴圈輸入組合(若有前綴詞)
for combo in combos:
    invite_code = "前綴詞" + ''.join(combo)
    
    # 找到輸入框並輸入邀請碼
    input_element = driver.find_element(By.XPATH, '輸入框路徑')
    input_element.clear()
    input_element.send_keys(invite_code)

    # 模擬按下 Enter 鍵
    input_element.send_keys(Keys.RETURN)
    # 輸入後再次回到輸入框網頁
    driver.get("輸入欄位的網址")

driver.close()