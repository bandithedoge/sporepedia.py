import SporeAPICoreUtils as spore
import requests
from bs4 import BeautifulSoup as bs

id = "501092584982"
cast_xml = requests.get(spore.AssetsForSporeCastURL(id, 0, 5000)).text
assets = []

for asset in bs(cast_xml, 'xml').find_all("id"):
    assets.append(str(asset)[4:16])

for asset_id in assets:
    xml = requests.get(spore.XMLURL(asset_id)).text
    spore.FetchAndSaveSmallPNG(asset_id)
    for asset in bs(xml, 'xml').find_all("asset"):
        spore.FetchAndSaveSmallPNG(str(asset)[7:19])
