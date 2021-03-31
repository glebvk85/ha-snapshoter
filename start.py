from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import smbclient
from PIL import Image
from io import BytesIO
import json

with open('config.json') as json_file:
    data = json.load(json_file)
    settings = data['options']

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
for i in settings['shots']:
    driver.get(
        f'https://yandex.ru/pogoda/maps/nowcast?via=mmapw&le_Lightning=1&lat={i["lat"]}&lon={i["lon"]}&z={i["zoom"]}')

    time.sleep(settings.get('sleep', 30))
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    im = im.crop((int(im.size[0] * i['crop_left_ratio']), int(im.size[1] * i['crop_top_ratio']), int(im.size[0] * i['crop_right_ratio']), int(im.size[1] * i['crop_bottom_ratio'])))
    im.save(i['image'])
    smbclient.register_session(settings['smb_server'], username=settings['smb_username'], password=settings['smb_password'])
    with smbclient.open_file(i['smb_path'] + "\\" + i['image'], mode="wb") as fd:
        file = open(i['image'], "rb")
        data = file.read()
        fd.write(data)

    print(driver.title)

driver.quit()
