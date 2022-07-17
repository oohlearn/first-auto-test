from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
#EC代表expected_conditions，設定縮寫，後面就可以用EC

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('http://the-internet.herokuapp.com')   #先載入想要檢查的網頁
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
        ))
    form_auth_link.click()

    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')
    ))
    username.send_keys('tomsmith')
    #尋找username的element，然後輸入tomsmith

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')
    #尋找password的element，輸入那串密碼

    driver.find_element(By.CSS_SELECTOR, 'button[type= submit]').click()
    #尋找登入按鈕的element，然後執行click的Mehtod

    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Logout')
    )).click()
    #登入進去後，畫面會切換（所以加上wait method）開始尋找logout，然後執行click

    flash = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')
    ))
    #假設登出之後，會畫面切換，並跳出一個快閃訊息，告訴登出成功，找出這個flash element
    assert 'logged out' in flash.text
    #  猜測在flash 裡面會有logged out的字串→就可以表示登出成功
    # （如果這個假設錯誤，就會有excetption被提出）

finally:
    driver.quit()