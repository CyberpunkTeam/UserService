from json import loads
from typing import Optional, List

from pydantic import BaseModel

from app.models.education import Education
from app.models.work_experience import WorkExperience


class Users(BaseModel):
    uid: str
    name: str
    lastname: str
    email: str
    location: str
    education: Optional[List[Education]] = []
    work_experience: Optional[List[WorkExperience]] = []
    profile_image: Optional[str] = ""
    cover_image: Optional[str] = ""
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""

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
            "created_date": str,
            "updated_date": str,
            "education": list,
            "work_experience": list,
        }

    def get_id(self):
        return self.uid
