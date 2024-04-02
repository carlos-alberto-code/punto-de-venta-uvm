from sqlalchemy.orm import DeclarativeMeta
from dataclasses import dataclass


@dataclass
class ModelAttributes:
    name: str
    type: str
    is_pk: bool
    is_required: bool

class Models:
    _instance = None
    _models = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Models, cls).__new__(cls)
        return cls._instance

    def __init__(self, *models: DeclarativeMeta):
        # self._models = {model.__name__.lower(): model for model in models}
        self. _models = {
            model.__class__.__name__.lower(): [
        }
    
    def __getitem__(self, key: str) -> ModelAttributes:
        return self._models[key.lower()]