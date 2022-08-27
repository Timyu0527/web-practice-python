from typing import final
from xml.dom.minidom import Document
import requests
from bs4 import BeautifulSoup
from entity.sight import Sight

class KeelungSightsCrawler:
    def __init__(self):
        self.__baseUrl = "https://www.travelking.com.tw"
        self.__allSightsURLs = []
        self.__allSights = []
        self.__getAllSightsURL()
        self.__getAllSightsInfo()

    def __getAllSightsURL(self):
        document = BeautifulSoup(requests.get("{}/tourguide/taiwan/keelungcity/".format(self.__baseUrl)).text, "html.parser")
        sel = document.select("div.box h4")
        for row in sel:
            sight = row.next_sibling
            for url in sight.select("li a"):
                self.__allSightsURLs.append(url["href"])

    def __getSightName(self, document):
        content = document.select("h1.h1")[0]
        if content == None:
            return ""
        return content.text

    def __getPhotoURL(self, document, url):
        photoURLs = document.select("div.gpic img")
        if photoURLs.__len__() == 0:
            return ""
        # print(photoURLs)
        return photoURLs[0]["data-src"]

    def __getDescription(self, document):
        content = document.select("div.text")[0]
        if content == None:
            return ""
        return content.text

    def __getZone(self, document):
        content = document.select("li.bc_last a")[0]
        if content == None:
            return ""
        return content.text

    def __getCategory(self, document):
        content = document.select("cite span strong")[0]
        if content == None:
            return ""
        return content.text

    def __getAddress(self, document):
        content = document.select("div.address p")[0]
        if content == None:
            return ""
        return content.text

    def __getAllSightsInfo(self):
        id = 1
        for sightUrl in self.__allSightsURLs:
            document = BeautifulSoup(requests.get("{}{}".format(self.__baseUrl, sightUrl)).text, "html.parser")
            sightName = self.__getSightName(document)
            category = self.__getCategory(document)
            zone = self.__getZone(document)
            photoURL = self.__getPhotoURL(document, sightUrl)
            description = self.__getDescription(document)
            address = self.__getAddress(document)
            self.__allSights.append(Sight(id, sightName, zone, category, photoURL, description, address))
            id += 1

    def getItem(self, zone):
        return [sight for sight in self.__allSights if sight.getZone() == "{}區".format(zone)]



