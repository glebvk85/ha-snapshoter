#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from PIL import Image
from io import BytesIO
import json

with open('/data/options.json') as json_file:
    settings = json.load(json_file)

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
for i in settings['shots']:
    driver.get(
        f'https://yandex.ru/pogoda/maps/nowcast?via=mmapw&le_Lightning=1&lat={i["lat"]}&lon={i["lon"]}&z={i["zoom"]}')

    time.sleep(i.get('sleep', 30))
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    im = im.crop((int(im.size[0] * i['crop_left_ratio']), int(im.size[1] * i['crop_top_ratio']), int(im.size[0] * i['crop_right_ratio']), int(im.size[1] * i['crop_bottom_ratio'])))
    im.save(i['image'])
    print(driver.title)

driver.quit()
