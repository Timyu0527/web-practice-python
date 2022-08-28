
from pydantic import BaseModel

class Sight(BaseModel):
    sightName: str
    zone: str
    category: str
    photoUrl: str
    description: str
    address: str

    def __str__(self):
        return  "sightName: {}\n" \
                "Zone: {}\n" \
                "Category: {}\n" \
                "PhotoURL: {}\n" \
                "Description: {}" \
                "Address: {}\n" \
                .format(
                    self.sightName,
                    self.zone,
                    self.category,
                    self.photoUrl,
                    self.description,
                    self.address
                )
    