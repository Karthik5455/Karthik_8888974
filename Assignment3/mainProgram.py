# Importing required libraries

# pip install selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
#maximizing the window
driver.maximize_window()

# Navigating to www.nofrills.ca website
driver.get("https://www.nofrills.ca/")
time.sleep(5)

#Close notification
closeNotification=driver.find_element("xpath","//button[normalize-space()='close']").click()
# Changing the location to waterloo
location=driver.find_element("xpath","//div[@class='fulfillment-mode-button__content']").click()
time.sleep(2)
changelocatin=driver.find_element("xpath","//a[normalize-space()='No, change location']").click()
time.sleep(3)
address=driver.find_element("xpath","//input[@id='location-search__search__input']")
address.click()
time.sleep(3)
address.send_keys("Waterloo")
address.send_keys(Keys.RETURN)
time.sleep(4)

#Select the store location
selectLocation=driver.find_element("xpath","(//button[@class='location-set-store__button location-set-store__button--is-not-current-location location-set-store__button--is-shoppable location-set-store__button--is-store location-set-store__button--is-not-this-banner'][normalize-space()='Select location'])[1]").click()
time.sleep(3)

#Handling the popup
actions = ActionChains(driver)
actions.send_keys(Keys.RETURN)
actions.perform()

#Finding the deals
deals = driver.find_element("xpath","//span[normalize-space()='Flyers & Deals']").click()
time.sleep(3)
allDeals=driver.find_element("xpath","//a[@data-code='/deals/all']").click()
time.sleep(3)
driver.execute_script("scroll(0,500)")

#Finding No Name brand
brand=driver.find_element("xpath","//button[normalize-space()='Brand']").click()
time.sleep(3)
selectBrand=driver.find_element("xpath","//label[normalize-space()='No Name']").click()
time.sleep(3)

#Sorting out from Low to High
relevance=driver.find_element("xpath","//button[@class='styled-dropdown__selected-item-link styled-dropdown__selected-item-link--filter']").click()
time.sleep(3)
sort=driver.find_element("xpath","//button[normalize-space()='Price (Low to High)']").click()
time.sleep(3)

driver.execute_script("scroll(0,1000)")
time.sleep(4)

#Adding an item to cart
addItem1=driver.find_element("xpath","//button[@aria-label='Add to cart, Soup Cups, Beef']").click()
time.sleep(3)

#Handling popups
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(1)
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(3)

#Checking cart
cart=driver.find_element("xpath","//button[@alt='Review Cart']")
cart.click()
time.sleep(3)

#Close cart
cart.click()
time.sleep(2)

driver.close()