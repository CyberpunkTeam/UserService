from json import loads
from typing import Optional, List

from pydantic.main import BaseModel


class Skills(BaseModel):
    programming_language: Optional[List[str]] = []
    frameworks: Optional[List[str]] = []
    platforms: Optional[List[str]] = []
    cloud_providers: Optional[List[str]] = []
    databases: Optional[List[str]] = []
    methodologies: Optional[List[str]] = []

    @staticmethod
    def get_schema():
        return {
            "programming_language": list,
            "frameworks": list,
            "platforms": list,
            "cloud_providers": list,
            "databases": list,
            "methodologies": list,
        }

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
