from dataclasses import dataclass, field

@dataclass
class Ingredient:
    names: list[str]
    names_string: str = ""

    # A method that returns the hash value of the ingredient object
    def __hash__(self) -> int:
        return hash(self.names[0])

    # A method that compares the ingredient object with another object for equality
    def __eq__(self, other) -> bool:
        return isinstance(other, Ingredient) and self.names_string == other.names_string
    
    def __postinit__(self) -> None:
        self.all_names_to_one_string()
        self.get_hash_from_all_names()
        
    def all_names_to_one_string(self):
        for i in self.names:
            self.names_string += f"{i}"

    def get_hash_from_all_names(self):
        return hash(self.names_string)