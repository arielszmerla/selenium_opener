import time

import os
import signal
from threading import Event

import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait


try:
    os.system("taskkill /im chrome.exe /f")
    name_upay = "ariel@upay.co.il"
    password_upay = "ariel1994"
    username = "steve"
    password = "upay@2012"
    driver_location = "C:\\Users\\ariel\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe"
    options = ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/ariel/AppData/Local/Google/Chrome/User Data")
    options.add_argument("profile-directory=default")
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(driver_location, options=options)

    driver.maximize_window()
    driver.get("https://app.upay.co.il/admin/")
    driver.implicitly_wait(5)

    currentWindow = driver.current_window_handle

    id_element = driver.find_element(by=By.ID, value="login_username")
    id_element.send_keys(name_upay)

    PW_UPAY = driver.find_element(by=By.ID, value="login_password")
    PW_UPAY.send_keys(password_upay)
    enter = driver.find_element(by=By.ID, value="login-form-submit")
    print(enter.is_enabled())
    enter.send_keys("\n")
    assert len(driver.window_handles) == 1
    driver.switch_to.new_window('tab')
    driver.get("http://84.95.87.35/phpmyadmin2/")
    id_element = driver.find_element(by=By.ID, value="input_username")
    id_element.send_keys(username)

    pw = driver.find_element(by=By.ID, value="input_password")
    pw.send_keys(password)
    i = 0

    go = driver.find_element(by=By.ID, value="input_go")
    id_element.submit()

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 2

    # Click the link which opens in a new window
    # driver.find_element(by=By.LINK_TEXT, value="new window").click()
    # Wait for the new window or tab
    driver.switch_to.new_window('tab')

    driver.get("http://80.179.148.52/phpmyadmin/")
    id_element = driver.find_element(by=By.ID, value="input_username")
    id_element.send_keys(username)

    pw = driver.find_element(by=By.ID, value="input_password")
    pw.send_keys(password)
    go = driver.find_element(by=By.ID, value="input_go")
    go.submit()
    assert len(driver.window_handles) == 3
    driver.switch_to.new_window('tab')
    driver.get("https://mail.google.com/mail/u/2/#inbox")
    os.startfile("Postman.lnk")
    os.startfile("C:\\Program Files\\NetBeans-12.6\\netbeans\\bin\\netbeans64.exe")
    os.startfile("putty.exe")
    os.startfile("putty.txt")
    a = 2
except:
    pass
