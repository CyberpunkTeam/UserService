from json import loads
from pydantic import BaseModel


class Locations(BaseModel):
    country: str
    city: str

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "country": str,
            "city": str,
        }

    def get_id(self):
        return self.country + self.city
