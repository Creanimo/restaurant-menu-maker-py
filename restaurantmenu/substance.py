from dataclasses import dataclass

# A class that represents any kind of substance that can be associated with an ingredient
@dataclass(frozen=True)
class Substance:
    name: str
    inline_icon: str

# A class that represents an allergen, which is a subclass of substance
@dataclass(frozen=True)
class Allergen(Substance):
    pass

# A class that represents an additive, which is a subclass of substance
@dataclass(frozen=True)
class Additive(Substance):
    code: str