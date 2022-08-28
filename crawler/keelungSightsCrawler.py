import requests
from bs4 import BeautifulSoup
from models.sight import Sight

class KeelungSightsCrawler:
    def __init__(self):
        self.__baseUrl = "https://www.travelking.com.tw"
        self.__allSightsURLs = []
        self.__allSights = []
        self.__getAllSightsURL()
        self.__getAllSightsInfo()

    def __getAllSightsURL(self):
        document = BeautifulSoup(requests.get(self.__baseUrl + "/tourguide/taiwan/keelungcity/").text, "html.parser")
        sel = document.select("div.box h4")
        for row in sel:
            sight = row.next_sibling
            for url in sight.select("li a"):
                self.__allSightsURLs.append(url["href"])

    def __getSightName(self, document: BeautifulSoup):
        content = document.select("h1.h1")[0]
        if content == None:
            return ""
        return content.text

    def __getPhotoURL(self, document: BeautifulSoup):
        photoURLs = document.select("div.gpic img")
        if len(photoURLs) == 0:
            return ""
        return photoURLs[0]["data-src"]

    def __getDescription(self, document: BeautifulSoup):
        content = document.select("div.text")[0]
        if content == None:
            return ""
        return content.text

    def __getZone(self, document: BeautifulSoup):
        content = document.select("li.bc_last a")[0]
        if content == None:
            return ""
        return content.text

    def __getCategory(self, document: BeautifulSoup):
        content = document.select("cite span strong")[0]
        if content == None:
            return ""
        return content.text

    def __getAddress(self, document: BeautifulSoup):
        content = document.select("div.address p")[0]
        if content == None:
            return ""
        return content.text

    def __getAllSightsInfo(self):
        for sightUrl in self.__allSightsURLs:
            document = BeautifulSoup(requests.get(self.__baseUrl + sightUrl).text, "html.parser")
            sightName = self.__getSightName(document)
            category = self.__getCategory(document)
            zone = self.__getZone(document)
            photoUrl = self.__getPhotoURL(document)
            description = self.__getDescription(document)
            address = self.__getAddress(document)
            self.__allSights.append(Sight(
                                        sightName=sightName,
                                        zone=zone,
                                        category=category,
                                        photoUrl=photoUrl,
                                        description=description,
                                        address=address
                                    ))

    # def getItem(self, zone: str):
    #     return [sight for sight in self.__allSights if sight.dict()['zone'] == "{}區".format(zone)]

    def getAllSight(self):
        self.__allSightsURLs = []
        sights = self.__allSights.copy()
        self.__allSights = []
        return sights



