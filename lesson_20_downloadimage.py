# Функция скачивания изображений

import random
import urllib.request

def downdload_img(url):
    name = random.randrange(1,100)
    name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, name)

downdload_img('http://otdeln.ru/wp-content/uploads/2020/11/6f9de30ae41309c2cbe6ddc7bccdbec0.png')