from typing import Optional, List
from json import loads
from pydantic import BaseModel

from app.models.education import Education
from app.models.skills import Skills
from app.models.work_experience import WorkExperience


class UserUpdate(BaseModel):
    uid: Optional[str] = ""
    name: Optional[str] = ""
    lastname: Optional[str] = ""
    location: Optional[str] = ""
    profile_image: Optional[str] = ""
    cover_image: Optional[str] = ""
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""
    education: Optional[List[Education]] = []
    work_experience: Optional[List[WorkExperience]] = []
    skills: Optional[Skills]
    idioms: Optional[List[str]]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
