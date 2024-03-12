from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy import inspect

from dataclasses import dataclass
from typing import List


@dataclass
class ModelFields:
    """
    This @dataclass is responsible for storing the fields of a model.
    Knowing the fields of a model and other metadata is useful for form creation.
    This way we can determine if:
    - A field is required or not, which allows us to handle the logic in the UI better.
    - A field is a primary key and should not be shown in the form.
    - The data type of the field to configure appropriate controls that allow
    validated input for each data type.
    
    TODO: The next feature of this component is to detect foreign keys to implement
    dropdowns that allow selecting information when it exists.
    
    Attributes:
        name (str): The name of the field.
        type (str): The data type of the field.
        is_nullable (bool): Indicates if the field can be nullable.
        is_primary_key (bool): Indicates if the field is a primary key.
        is_foreign_key (bool): Indicates if the field is a foreign key. (Not used yet)
    """
    name: str
    type: str
    is_nullable: bool
    is_primary_key: bool
    # is_foreign_key: bool


class FormModelController:

    def __init__(self, model: DeclarativeMeta) -> None:
        self._model = model
    

    @property
    def model_attributes(self) -> List[ModelFields]:
        return [
            ModelFields(
                name=column.name,
                type=str(column.type),
                is_nullable=bool(column.nullable),
                is_primary_key=column.primary_key,
                # is_foreign_key=False,  # Set the default value for is_foreign_key
            ) for column in inspect(self._model).columns
        ]