import pandas
from dataclasses import dataclass
from typing import Callable

def split_by_store(fileLocation: str, saveLocation: str):
    print(fileLocation, saveLocation)
    pass

@dataclass
class Procedure:
    btn: str
    func: Callable
    desc: str = ""

procedures = [
    Procedure(
        "Split by store types",
        split_by_store,
        "Splits purchases based on the type of store they have been purchased at."
    )
]