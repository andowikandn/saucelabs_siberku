from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android.uiautomator2.base import UiAutomator2Options

options = UiAutomator2Options()

options.udid = "RR8M90AYT8N"
options.platform_name = "Android"
options.app_package = "com.swaglabsmobileapp"
options.app_activity = "com.swaglabsmobileapp.MainActivity"

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 
'test-Username').send_keys('standard_user')
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 
'test-Password').send_keys('secret_sauce')
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 
'test-LOGIN').click()

