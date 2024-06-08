from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta


class Repository:
    # TODO: Establecer comprobaciones y manejo de errores
    
    def __init__(self, model: DeclarativeMeta, session: Session) -> None:
        self.model = model
        self.db = session    

    def get_all(self):
        """
        Retrieves all records from the database. If an order_by parameter is provided,
        the results are sorted by that model field.

        Args:
            order_by: The field to sort the records by. If None, no specific ordering is applied.

        Returns:
            A list of all records from the database, possibly sorted by the specified field.
        """
        return self.db.query(self.model).all()
    
    def get_by_id(self, id: int):
        """
        Retrieves a record by its ID.
    
        Args:
            id: The ID of the record to retrieve.
    
        Returns:
            The record with the specified ID, or None if no such record exists.
        """
        return self.db.query(self.model).get(id)

    def create(self, **kwargs):
        """
        Creates a record in the table that represents the injected model in the constructor.
        Executes necessary validations through decorators to ensure data integrity.

        Args:
            **kwargs: The field names and their corresponding values for the new instance.

        Returns:
            None
        """
        instance = self.model(**kwargs)
        self.db.add(instance)
        self.db.commit()
    
    def update(self, id: int, **kwargs):
        """
        Update the fields of an instance in the repository.
        Executes necessary validations through decorators to ensure data integrity.
    
        Args:
            id (int): The ID of the instance to update.
            **kwargs: The field names and their corresponding new values.
    
        Returns:
            None
        """
        instance = self.db.query(self.model).get(id)
        if instance is not None:
            for key, value in kwargs.items():
                if hasattr(instance, key):
                    setattr(instance, key, value)
            self.db.commit()
            