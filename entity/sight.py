from email.utils import getaddresses


class Sight:
    def __init__(
        self,
        id: int,
        sightName: str,
        zone: str,
        category: str,
        photoURL: str,
        description: str,
        address: str,
    ):
        self.__id = id
        self.__sightName = sightName
        self.__zone = zone
        self.__category = category
        self.__photoURL = photoURL
        self.__description = description
        self.__address = address
        
    def getSightName(self):
        return self.__sightName
    
    def getZone(self):
        return self.__zone
    
    def getCategory(self):
        return self.__category
    
    def getPhotoURL(self):
        return self.__photoURL
    
    def getDescription(self):
        return self.__description
    
    def getAddress(self):
        return self.__address

    def __str__(self):
        return  "sightName: {}\n" \
                "Zone: {}\n" \
                "Category: {}\n" \
                "PhotoURL: {}\n" \
                "Description: {}" \
                "Address: {}\n" \
                .format(
                    self.getSightName(),
                    self.getZone(),
                    self.getCategory(),
                    self.getPhotoURL(),
                    self.getDescription(),
                    self.getAddress()
                )
    