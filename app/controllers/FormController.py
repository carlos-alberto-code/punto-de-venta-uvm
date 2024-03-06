from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy import inspect

from dataclasses import dataclass


@dataclass
class FieldInfo:
    nullable: bool
    name: str
    type: str
    pk: bool


class FormController:

    def __init__(self, model: DeclarativeMeta) -> None:
        self._model = model

    @property
    def metadata(self):
        inspector = inspect(self._model)
        fields_info = []
        for column in inspector.c:
            info = FieldInfo(
                name=str(column.name),
                type=str(column.type),
                pk=bool(column.primary_key),
                nullable=bool(column.nullable)
            )
            fields_info.append(info)
        return fields_info
    