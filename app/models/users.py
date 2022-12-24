from json import loads
from typing import Optional

from pydantic import BaseModel


class Users(BaseModel):
    uid: str
    name: str
    lastname: str
    email: str
    location: str
    profile_image: Optional[str] = ""
    cover_image: Optional[str] = ""

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    def set_default_images(self):
        if self.cover_image == "":
            self.cover_image = "default"

        if self.profile_image == "":
            self.profile_image = "default"

    @staticmethod
    def get_schema():
        return {
            "name": str,
            "lastname": str,
            "email": str,
            "location": str,
            "uid": str,
            "profile_image": str,
            "cover_image": str,
        }
