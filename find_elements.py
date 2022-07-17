from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
try:
    driver.get('http://the-internet.herokuapp.com')   #先載入想要檢查的網頁
    driver.find_element(By.LINK_TEXT, 'Form Authentication')  #尋找特定元素，但沒有作後續處理(所以沒有設定變數)
    
    els = driver.find_elements(By.TAG_NAME, 'a')   #測試所有TAG為'a'(尋找在那個網頁裡的所有連結)
    print(f'There were {len(els)} anchor elements')  #因為會變成清單，印出清單的長度(總共有幾個連結)
    
    els = driver.find_elements(By.TAG_NAME, 'foo')  #測試若尋找不存在的TAG
    print(f'There were {len(els)} foo elements')
finally:
    driver.quit()