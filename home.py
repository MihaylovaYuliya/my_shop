import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0,600);")

book_selenium = driver.find_element(By.CSS_SELECTOR, "img[title='Selenium Ruby']")
book_selenium.click()

reviews_btn = driver.find_element(By.CSS_SELECTOR, "li.reviews_tab")
reviews_btn.click()
rating_tab = driver.find_element(By.CLASS_NAME, "star-5")
rating_tab.click()

comment_field = driver.find_element(By.ID, "comment")
comment_field.send_keys("Nice book!")
time.sleep(3)
name_field = driver.find_element(By.ID, "author")
name_field.send_keys("Yuliya")
time.sleep(3)
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("yukka83@gmail.com")
time.sleep(3)
submit_btn = driver.find_element(By.CSS_SELECTOR, "input.submit")
submit_btn.click()
driver.quit()
