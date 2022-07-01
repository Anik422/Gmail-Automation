from time import sleep
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc



if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get('https://accounts.google.com/')
    # driver.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    mail_box = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    mail_box.send_keys("nirmal.mahata4090@gmail.com")
    mail_box_next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span') 
    mail_box_next.click()
    sleep(300)
    driver.close()