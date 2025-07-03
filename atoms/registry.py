import json
import os
from .atom import Atom

file_path = os.path.join(os.path.dirname(__file__), '../assets/atoms.json')

AtomRegistry = []

with open(file_path, encoding='utf-8') as f:
    data = json.load(f)
    for element in data:
        atom = Atom(
            symbol=element["symbol"],
            name=element["name"],
            atomic_number=element["atomicNumber"],
            mass=element["mass"],
            electrons=element["electrons"],
            color=element["color"]
        )
        AtomRegistry.append(atom)

if __name__ == "__main__":
    for atom in AtomRegistry:
        print(f"{atom.atomic_number}: {atom.symbol} - {atom.name}")
