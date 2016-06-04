import requests
from bs4 import BeautifulSoup
from datetime import datetime
import shutil
import time
from IPython.display import Image
from random import randint

ori = requests.get("https://www.ris.gov.tw/id_card/")
soup = BeautifulSoup(ori.text)
key =  soup.select('#captchaKey')[0]["value"]

rs = requests.session()
url = "https://www.ris.gov.tw/apply/captcha/image?CAPTCHA_KEY=" + key
time =  str(int((time.time())*100)) + str(randint(0,9))
url += "&time=" + time

res = rs.get(url, headers={'referer': 'https://www.ris.gov.tw/id_card/'})
with open('check.jpg', 'wb') as jpeg_file:
    jpeg_file.write(res.content)



data = {
captchaKey: "bf0426b551fc4157bb7cc8da87f5a978",
idnum: "A123124141",
applyTWY: "105",
applyMM:"2",
applyDD:"3",
siteId:"10001",
applyReason:"2",
captchaInput:"6D83S"
}