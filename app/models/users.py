from json import loads

from pydantic import BaseModel


class Users(BaseModel):
    name: str
    lastname: str
    email: str
    location: str

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {"name": str, "lastname": str, "email": str, "location": str}
