import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
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
shop_tap = driver.find_element(By.ID, "menu-item-40")
shop_tap.click()
time.sleep(3)
"""отображение страницы товара"""
# open_book_html = driver.find_element(By.CSS_SELECTOR, "img[title='Mastering HTML5 Forms'] ")
# open_book_html.click()
# time.sleep()
# book_header = driver.find_element(By.CSS_SELECTOR, "h1[itemprop='name']")
# book_header_text = book_header.text
# assert "HTML5 Forms" in book_header_text
"""Количество товаров в категории"""
# category_html = driver.find_element(By.CSS_SELECTOR, "li.cat-item.cat-item-19")
# category_html.click()
# books_count = driver.find_elements(By.CSS_SELECTOR, "a > h3")
# assert len(books_count) == 3
"""Сортировка товаров"""
# default_selector = driver.find_element(By.CSS_SELECTOR, "option[value='menu_order']")
# default_selector_selected = default_selector.get_attribute("value")
# assert default_selector_selected == "menu_order"
# selector_element = driver.find_element(By.CLASS_NAME, "orderby" )
# select = Select(selector_element)
# select.select_by_value("price-desc")
# price_desc_selector = driver.find_element(By.CSS_SELECTOR, "option[value='price-desc']")
# price_desc_selector_selected = price_desc_selector.get_attribute("value")
# assert price_desc_selector_selected == "price-desc"
"""Отображение , скидка товара"""
# open_book_android = driver.find_element(By.CSS_SELECTOR, "img[title ='Android Quick Start Guide']")
# open_book_android.click()
# book_old_price = driver.find_element(By.CSS_SELECTOR, ".price > del >span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element(By.CSS_SELECTOR, ".price >ins> span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_covering = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_covering.click()
# book_covering_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
# book_covering_close.click()
"""проверка цены в корзине"""
# add_to_cart_book = driver.find_element(By.CSS_SELECTOR, "a[data-product_id='182']")
# add_to_cart_book.click()
# item = driver.find_element(By.CSS_SELECTOR, "span[class ='cartcontents']")
# item_text = item.text
# assert item_text == "1 Item"
# amount = driver.find_element(By.CSS_SELECTOR, "span[class='amount']")
# amount_text = amount.text
# assert amount_text == "₹180.00"
# subtotal = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "₹180.00"))
# total = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total"), "₹183.60"))
"""работа в корзине"""
# driver.execute_script("window.scrollBy(0,300);")
# add_to_cart_book = driver.find_element(By.CSS_SELECTOR, "a[data-product_id='182']")
# add_to_cart_book.click()
# time.sleep(3)
# add_second_book = driver.find_element(By.CSS_SELECTOR, "a[data-product_id='180']")
# add_second_book.click()
# cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
# cart.click()
# time.sleep(3)
# delete_book_1 = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1)")
# delete_book_1.click()
# time.sleep(3)
# undo_tap = driver.find_element(By.CSS_SELECTOR, ".woocommerce-message > a")
# undo_tap.click()
# quantity = driver.find_element(By.CSS_SELECTOR, "div.quantity")
# quantity.clear()
# quantity_add = driver.find_element(By.CSS_SELECTOR, "div.quantity")
# quantity_add.send_keys("3")
# update_btn = driver.find_element(By.CSS_SELECTOR, "input[name='update_cart']")
# update_btn.click()
# quantity_check = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty.text")
# quantity_total = quantity_check.get_attribute("value")
# assert quantity_check == "3"
# apply_coupon_btn = driver.find_element(By.CSS_SELECTOR, "input[name='apply_coupon']")
# apply_coupon_btn.click()
# error = driver.find_element(By.CLASS_NAME, "woocommerce-error")
# error_msg = error.text
# assert error_msg == "Please enter a coupon code."
"""покупка товара"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop_tap = driver.find_element(By.ID, "menu-item-40")
# shop_tap.click()
# time.sleep(3)
# add_to_cart_book = driver.find_element(By.CSS_SELECTOR, "a[data-product_id='182']")
# add_to_cart_book.click()
# cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
# cart.click()
# checkout_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                                                            "a.checkout-button.button.alt.wc-forward"))) # не проходит
# checkout_btn.click()
# first_name_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name_field.send_keys("Yuliya")
# input_last_name_field = driver.find_element(By.ID, "billing_last_name_field")
# input_last_name_field.send_keys("Win")
# input_email_field = driver.find_element(By.ID, "billing_email_field")
# input_email_field.send_keys("yukka83@gmail.com")
# input_phone_field = driver.find_element(By.ID, "billing_email_field")
# input_phone_field.send_keys("79211111111")
# country = driver.find_element(By.ID, "s2id_billing_country")
# country.click()
# country_search = driver.find_element(By.ID, "s2id_autogen1_search")
# country_search.send_keys("India")
# country_field_search = driver.find_element(By.ID, "select2-chosen-1")
# country_field_search.click()
# adress_field = driver.find_element(By.ID, "billing_address_1")
# adress_field.send_keys("badaeva")
# city_field = driver.find_element(By.ID, "billing_city")
# city_field.send_keys("Goa")
# state_country_selector = driver.find_element(By.ID, "s2id_billing_state")
# state_country_selector.click()
# input_country = driver.find_element(By.ID, "s2id_autogen2_search")
# input_country.send_keys("Kerala")
# country_field = driver.find_element(By.CSS_SELECTOR, "span.select2-match")
# country_field.click()
# postcode_field = driver.find_element(By.ID, "billing_postcode")
# postcode_field.send_keys("193318")
# driver.execute_script("window.scrollBy(0,600);")
# check_payments = driver.find_element(By.ID, "payment_method_cheque")
# check_payments.click()
# place_order_btn = driver.find_element(By.ID, "place_order")
# place_order_btn.click()
# message = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
#                                      "Thank you. Your order has been received."))
# pay_method = WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Direct Bank Transfer"))



