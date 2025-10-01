from dataclasses import dataclass

@dataclass
class Pokemon:
    name:str
    id:int
    type:str

test = Pokemon("Lucario", "119", "Lutador")
print(type(test))
print(test)