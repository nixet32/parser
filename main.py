from bs4 import BeautifulSoup
import requests
import datetime
import json


class Letak:
    def __init__(self, title, thumbnail, shop_name, valid_from, valid_to):
        self.title = title
        self.thumbnail = thumbnail
        self.shop_name = shop_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.parsed_time = datetime.datetime.now()

    def to_dict(self):
        return {
            "title": self.title,
            "thumbnail": self.thumbnail,
            "shop_name": self.shop_name,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "parsed_time": self.parsed_time.strftime("%Y-%m-%d %H:%M:%S")
        }


url = "https://www.prospektmaschine.de/hypermarkte/"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

articles = doc.find_all(class_="brochure-thumb col-xs-6 col-sm-3")

letaky = []

for article in articles:
    title_element = article.find(class_="grid-item-content")
    thumbnail_element = article.find(class_="img-container")
    shop_element = article.find(class_="grid-logo")

    title = title_element.strong.getText()
    thumbnail = thumbnail_element.img.get('src') or thumbnail_element.img.get('data-src')
    shop_name = shop_element.img.get('alt')
    valid = article.find(class_="hidden-sm").getText()

    if '-' in valid:
        valid = valid.split('-')
        valid_from = valid[0].replace(" ", "")
        valid_to = valid[1]
    else:
        valid = valid.split()
        valid_from = valid[0] + " " + valid[1]
        valid_to = valid[2]

        # Ak by sme chceli iba dátumy v JSON súbore
        # valid = valid.split()
        # valid_from = ""
        # valid_to = valid[2]

    letaky.append(Letak(title, thumbnail, shop_name[5:], valid_from, valid_to))

json_data = json.dumps([letak.to_dict() for letak in letaky], indent=4)

with open("output.json", 'w') as f:
    f.write(json_data)
