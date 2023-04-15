from json import loads

from pydantic import BaseModel


class Agendas(BaseModel):
    aid: str
    following_uid: str
    agenda_type: str

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {"aid": str, "following_uid": str, "agenda_type": str}
