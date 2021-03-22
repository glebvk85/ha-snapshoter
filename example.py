from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
requests = 0
requests_stop = False
driver.get('https://yandex.ru/pogoda/maps/nowcast?via=mmapw&le_Lightning=1&lat=56.27602630491462&lon=44.20384500547761&ll=42.201072_56.259405&z=6')

time.sleep(30)

driver.save_screenshot("images/screenshot.png")



print(driver.title)

driver.quit()
