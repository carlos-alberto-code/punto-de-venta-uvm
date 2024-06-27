from typing import Optional


class Customer:
    
    def __init__(self, id: Optional[int], full_name: str, age: int, email: str) -> None:
        self.id         = id
        self.age        = age
        self.email      = email
        self.full_name  = full_name
    
    def __repr__(self) -> str:
        return f"Customer({self.id}, {self.full_name}, {self.age}, {self.email})"
    