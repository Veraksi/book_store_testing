from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


# driver.get("http://practice.automationtesting.in/")
# account = driver.find_element_by_id("menu-item-50")
# account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("woyeyo5059@arpizol.com")
# password = driver.find_element_by_id("password")
# password.send_keys("omd79cy")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# html5_forms = driver.find_element_by_css_selector("[title ='Mastering HTML5 Forms']")
# html5_forms.click()
# html5_forms_name = driver.find_element_by_tag_name("h1")
# html5_forms_name_text = html5_forms_name.text
# assert html5_forms_name_text == "HTML5 Forms"
driver.quit()

# driver.get("http://practice.automationtesting.in/")
# account = driver.find_element_by_id("menu-item-50")
# account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("woyeyo5059@arpizol.com")
# password = driver.find_element_by_id("password")
# password.send_keys("omd79cy")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# html = driver.find_element_by_link_text("HTML")
# html.click()
# items = driver.find_elements_by_class_name("product-type-simple")
# if len(items) == 3:
#     print("В категории 3 товара")
# else:
#     print("В категории другое количество товара")
driver.quit()

# driver.get("http://practice.automationtesting.in/")
# account = driver.find_element_by_id("menu-item-50")
# account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("woyeyo5059@arpizol.com")
# password = driver.find_element_by_id("password")
# password.send_keys("omd79cy")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# orderby = driver.find_element_by_name("orderby")
# select = Select(orderby)
# default = driver.find_element_by_css_selector("[value = 'menu_order']")
# default_selected = default.get_attribute("selected")
# select.select_by_value("price-desc")
# orderby = driver.find_element_by_name("orderby")
# desc = driver.find_element_by_css_selector("[value = 'price-desc']")
# desc_selected = desc.get_attribute("selected")
driver.quit()


# driver.get("http://practice.automationtesting.in/")
# account = driver.find_element_by_id("menu-item-50")
# account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("woyeyo5059@arpizol.com")
# password = driver.find_element_by_id("password")
# password.send_keys("omd79cy")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# android = driver.find_element_by_css_selector("[title ='Android Quick Start Guide']")
# android.click()
# old_price = driver.find_element_by_tag_name("del")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# new_price = driver.find_element_by_css_selector("ins>.woocommerce-Price-amount")
# new_price_text = new_price.text
# assert new_price_text == '₹450.00'
# android_img = WebDriverWait(driver, 5).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, "[title = 'Android Quick Start Guide']")))
# android_img.click()
# close = WebDriverWait(driver,5).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close.click()
driver.quit()

# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# add_to_bascet = driver.find_element_by_css_selector("[data-product_id = '182']")
# add_to_bascet.click()
# time.sleep(1)
# items = driver.find_element_by_class_name("cartcontents")
# items_text = items.text
# assert items_text == "1 Item"
# price = driver.find_element_by_class_name("amount")
# price_text = price.text
# assert price_text =="₹180.00"
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
# Subtotal = WebDriverWait(driver,5).until(
# EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-subtotal>.woocommerce-Price-amount")))
# Total = WebDriverWait(driver,5).until(
# EC.visibility_of_element_located((By.CSS_SELECTOR, "strong>.woocommerce-Price-amount")))
driver.quit()


# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5 = driver.find_element_by_css_selector("[data-product_id = '182']")
# html5.click()
# time.sleep(2)
# js_data = driver.find_element_by_css_selector("[data-product_id = '180']")
# js_data.click()
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
# time.sleep(2)
# delete = driver.find_element_by_class_name("remove")
# delete.click()
# time.sleep(2)
# undo = driver.find_element_by_link_text("Undo?")
# undo.click()
# quanity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quanity.clear()
# quanity.send_keys("3")
# update_basket = driver.find_element_by_name("update_cart")
# update_basket.click()
# quanity_text = quanity.get_attribute("value")
# assert quanity_text == "3"
# time.sleep(2)
# apply = driver.find_element_by_name("apply_coupon")
# apply.click()
# WebDriverWait(driver,5).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
driver.quit()


driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_link_text("Shop")
shop.click()
html5 = driver.find_element_by_css_selector("[data-product_id = '182']")
html5.click()
time.sleep(1)
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
WebDriverWait(driver, 5).until(
EC.visibility_of_element_located((By.CLASS_NAME, "checkout-button")))
Proceed = driver.find_element_by_class_name("checkout-button")
Proceed.click()
WebDriverWait(driver, 5).until(
EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Ivan")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Ivanov")
email = driver.find_element_by_id("billing_email")
email.send_keys("123@123.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("1234567890")
country = driver.find_element_by_id("select2-chosen-1")
country.click()
country_2 = driver.find_element_by_id("s2id_autogen1_search")
country_2.send_keys("Russia")
Russia = driver.find_element_by_id("select2-result-label-393")
Russia.click()
adress = driver.find_element_by_id("billing_address_1")
adress.send_keys("Ivanovskaya")
adress_2 = driver.find_element_by_id("billing_address_2")
adress_2.send_keys("3")
city = driver.find_element_by_id("billing_city")
city.send_keys("Ivanov")
State = driver.find_element_by_id("billing_state")
State.send_keys("Russia")
Postcode = driver.find_element_by_id("billing_postcode")
Postcode.send_keys("111111")
driver.execute_script("window.scrollBy(0, 600)")
time.sleep(2)
check = driver.find_element_by_id("payment_method_cheque")
check.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
WebDriverWait(driver,5).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
WebDriverWait(driver,5).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method>strong"), "Check Payments"))
driver.quit()
