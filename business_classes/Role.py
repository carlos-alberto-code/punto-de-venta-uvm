class Role:

    def __init__(self):
        self.__id: int = 0
        self.__name: str = ''
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name

    def __str__(self):
        return f"Role(name={self.name})"