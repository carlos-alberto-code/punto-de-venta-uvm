from sqlalchemy.orm import DeclarativeMeta
# from typing import List


class Models:

    def __init__(self, *models: DeclarativeMeta) -> None:
        self._models = {model.__class__.__name__.lower(): model for model in models}
    
    def __len__(self):
        return len(self._models)
    
    def __iter__(self):
        return iter(self._models.keys())
