import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# registration
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

# my_account_tab = driver.find_element(By.ID, "menu-item-50")
# my_account_tab.click()
# time.sleep(3)
# email_field = driver.find_element(By.CSS_SELECTOR, "input[id='reg_email']")
# email_field.send_keys("litlesparrow1983@gmail.com")
# time.sleep(3)
# password_field = driver.find_element(By.CSS_SELECTOR, "input[id='reg_password']")
# password_field.send_keys("Ipsec1983@")
# time.sleep(3)
# register_btn = driver.find_element(By.NAME, "register")
# register_btn.click()
# driver.quit()

# login
my_account_tab = driver.find_element(By.ID, "menu-item-50")
my_account_tab.click()
time.sleep(3)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("litlesparrow1983@gmail.com")
time.sleep(3)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Ipsec1983@")
time.sleep(3)
login_btn = driver.find_element(By.CSS_SELECTOR, "input[name='login']")
login_btn.click()
time.sleep(3)
logout_btn = driver.find_element(By.LINK_TEXT, "Logout")
logout_btn_text = logout_btn.text
assert "Logout" == logout_btn_text
