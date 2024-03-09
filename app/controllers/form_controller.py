from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy import inspect

from dataclasses import dataclass
from typing import List

import flet as ft


@dataclass
class ModelAttribute:
    name: str
    type: str
    is_primary: bool
    is_nullable: bool


class FormModelController:

    def __init__(self, model: DeclarativeMeta) -> None:
        self._model = model
    

    @ property
    def model_attibutes(self) -> List[ModelAttribute]:
        return [
            ModelAttribute(
                name=column.name,
                type=str(column.type),
                is_primary=column.primary_key,
                is_nullable=bool(column.nullable),
            ) for column in inspect(self._model).c
        ]