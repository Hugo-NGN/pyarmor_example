"""
Script utilisant le module utils obfusqué par PyArmor.
Le module obfusqué est dans le dossier dist/
"""

# Ajouter le dossier dist au path pour importer les modules obfusqués
import sys
from pathlib import Path

# Ajouter dist au chemin de recherche Python
dist_path = Path(__file__).parent / "dist"
sys.path.insert(0, str(dist_path))

# Importer depuis le module obfusqué
from utils.methods import MyClass

if __name__ == "__main__":
    print("=== module utils obfusqué ===\n")
    
    obj = MyClass(3, 5)
    print(f"Valeurs:[a={obj.a}, b={obj.b}]")
    print(f"Addition: {obj.add()}")
    print(f"Multiplication: {obj.multiply()}")
    print(f"Subtraction: {obj.subtract()}")
    print(f"Sum of Squares: {obj.sum_squares()}")
    
    print()
    print(help(MyClass))
