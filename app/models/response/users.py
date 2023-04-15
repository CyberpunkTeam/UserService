from typing import Optional, List

from pydantic.main import BaseModel

from app.models.education import Education
from app.models.skills import Skills
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
    skills: Optional[Skills]
    idioms: Optional[List[str]]
    followers: List[str]
    following: List[str]
