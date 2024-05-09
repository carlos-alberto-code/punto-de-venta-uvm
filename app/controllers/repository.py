from sqlalchemy.orm import Session
from .decorators    import (
    validate_id,
    validate_name,
    validate_unique_name,
)


class Repository:
    
    def __init__(self, model, session: Session) -> None:
        self.model = model
        self.db = session    

    def get_all(self):
            """
            Retrieves all records from the database sorted by name.

            Returns:
                A list of all records from the database sorted by name.
            """
            return self.db.query(self.model)\
            .order_by(self.model.name)\
            .all()

    @validate_unique_name
    @validate_name
    def create(self, name: str):
        """
        Creates a record in the table that represents the injected model in the constructor.
        Executes necessary validations through decorators to ensure data integrity.

        Args:
            name (str): The name of the instance.

        Returns:
            None
        """
        instance = self.model(name=name.lower())
        self.db.add(instance)
        self.db.commit()
    
    @validate_id
    def get_by_id(self, id: int):
        """
        Retrieves a record from the database by its ID.
        Executes necessary validations through decorators to ensure data integrity.

        Args:
            id (int): The ID of the record to retrieve.

        Returns:
            The record with the specified ID, or None if not found.
        """
        return self.db.query(self.model).get(id)
    
    # @validate_id
    # def delete(self, id: int):
    #     instance = self.db.query(self.model).get(id)
    #     self.db.delete(instance)
    #     self.db.commit()
    
    @validate_unique_name
    @validate_name
    @validate_id
    def update(self, id: int, new_name: str):
        """
        Update the name of an instance in the repository.
        Executes necessary validations through decorators to ensure data integrity.

        Args:
            id (int): The ID of the instance to update.
            new_name (str): The new name to assign to the instance.

        Returns:
            None
        """
        instance = self.db.query(self.model).get(id)
        if instance is not None:
            instance.name = new_name.lower()
            self.db.commit()
    
    def search(self, name: str):
            """
            Search for records in the database that match the given name.
            This method functions in GUI events in real-time.

            Args:
                name (str): The name to search for.

            Returns:
                list: A list of records that match the given name.
            """
            return self.db.query(self.model)\
                .filter(self.model.name.ilike(f'%{name}%'))\
                .order_by(self.model.name)\
                .all()
