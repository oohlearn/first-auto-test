from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
#EC代表expected_conditions，設定縮寫，後面就可以用EC

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('http://the-internet.herokuapp.com')   #先載入想要檢查的網頁
    #driver.find_element(By.LINK_TEXT, 'Form Authentication')  #尋找特定元素，但沒有作後續處理(所以沒有設定變數)
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')) 
    )
    #取代上面那行，並加入等待的功能
    # print(driver.current_url) 
    # 利用print的功能，印出現在selenium抓到的網址跟我們wait的url有沒有相同
    # 若不同，就會出現等待時間比我們想的久
    wait.until(EC.url_to_be('http://the-internet.herokuapp.com/'))

finally:
    driver.quit()