from dataclasses import dataclass

@dataclass
class Allergen:
    name: str
    inline_icon: str

    # A method that returns the hash value of the ingredient object
    def __hash__(self) -> int:
        return hash(self.name)

    # A method that compares the ingredient object with another object for equality
    def __eq__(self, other) -> bool:
        return isinstance(other, Ingredient) and self.name == other.name