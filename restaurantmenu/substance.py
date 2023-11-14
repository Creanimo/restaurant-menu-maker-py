from dataclasses import dataclass

# A class that represents any kind of substance that can be associated with an ingredient
@dataclass(frozen=True)
class Substance:
    name: str
    inline_icon: str

    # A method that returns the hash value of the substance object
    def __hash__(self) -> int:
        return hash(self.name)

    # A method that compares the substance object with another object for equality
    def __eq__(self, other) -> bool:
        return isinstance(other, Substance) and self.name == other.name

# A class that represents an allergen, which is a subclass of substance
@dataclass(frozen=True)
class Allergen(Substance):
    pass

# A class that represents an additive, which is a subclass of substance
@dataclass(frozen=True)
class Additive(Substance):
    code: str