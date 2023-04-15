from json import loads

from pydantic import BaseModel


class Agendas(BaseModel):
    uid: str
    following_uid: str

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {"uid": str, "following_uid": str}
