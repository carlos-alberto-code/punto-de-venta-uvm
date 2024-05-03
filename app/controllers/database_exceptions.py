class EmptyTableException(Exception):
    """
    Exception raised when a table is empty.

    Attributes:
        tablename (str): The name of the empty table.
    """

    def __init__(self, tablename: str):
        """
        Initializes a new instance of the EmptyTableException class.

        Args:
            tablename (str): The name of the empty table.
        """
        super().__init__(f'There is no data in the table "{tablename}".')


class ValueAlreadyExistsException(Exception):
    """
    Exception raised when a value already exists in a table.

    Attributes:
        item_name (str): The name of the item that already exists.
        tablename (str): The name of the table where the item already exists.
    """

    def __init__(self, item_name: str, tablename: str):
        super().__init__(f'The item "{item_name.lower()}" already exists in the table "{tablename}".')


class ValueNotFoundException(Exception):
    """
    Exception raised when a value is not found in a table.

    Attributes:
        item_name (str): The name of the item that was not found.
        tablename (str): The name of the table where the item was expected to be found.
    """

    def __init__(self, item_name: str, tablename: str):
        super().__init__(f'The item "{item_name.lower()}" does not exist in the table "{tablename}".')
