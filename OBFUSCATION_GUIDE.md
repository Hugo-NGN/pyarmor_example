# Guide d'obfuscation avec PyArmor

Ce guide explique comment obfusquer un répertoire Python avec PyArmor et l'utiliser dans vos scripts.

## Prérequis

Installer PyArmor dans votre environnement Python :

```bash
pip install pyarmor
```

## Étapes d'obfuscation

### 1. Structure initiale du projet

```
projet/
├── main.py
└── utils/
    ├── __init__.py
    └── methods.py
```

### 2. Obfusquer le répertoire

Exécutez la commande suivante depuis la racine du projet :

```bash
pyarmor gen --recursive utils
```

**Options disponibles :**
- `--recursive` : Obfusque tous les fichiers Python dans le répertoire et ses sous-dossiers
- `--output dist` : Spécifie le dossier de sortie (par défaut : `dist/`)

### 3. Structure après obfuscation

```
projet/
├── main.py
├── utils/                          # Code source original
│   ├── __init__.py
│   └── methods.py
└── dist/                            # Code obfusqué
    ├── pyarmor_runtime_000000/      # Runtime PyArmor (requis)
    │   └── pyarmor_runtime.so
    └── utils/                       # Module obfusqué
        ├── __init__.py
        └── methods.py               # Bytecode chiffré
```

## Utilisation du module obfusqué

### Option 1 : Script avec modification du sys.path

Créez un script qui importe depuis le dossier `dist/` :

```python
import sys
from pathlib import Path

# Ajouter dist/ au chemin de recherche Python
dist_path = Path(__file__).parent / "dist"
sys.path.insert(0, str(dist_path))

# Importer depuis le module obfusqué
from utils.methods import MyClass

if __name__ == "__main__":
    obj = MyClass(3, 5)
    print("Addition:", obj.add())
    print("Multiplication:", obj.multiply())
```

### Option 2 : Exécution avec PYTHONPATH

Modifier la variable d'environnement lors de l'exécution :

```bash
PYTHONPATH=./dist python main.py
```

### Option 3 : Distribution du code obfusqué

Pour distribuer votre application :

1. **Copiez uniquement le contenu de `dist/`** vers votre environnement de production
2. **Incluez le dossier `pyarmor_runtime_000000/`** (obligatoire)
3. Votre script peut maintenant importer normalement :

```python
from utils.methods import MyClass
```

## Distribution finale

Structure recommandée pour la distribution :

```
app_production/
├── main.py
├── pyarmor_runtime_000000/
│   └── pyarmor_runtime.so
└── utils/
    ├── __init__.py
    └── methods.py  (obfusqué)
```

## Points importants

1. **Ne pas supprimer `pyarmor_runtime_000000/`** : Ce dossier contient le runtime nécessaire à l'exécution du code obfusqué

2. **Garder le code source séparé** : Conservez votre code source original dans un endroit sécurisé, le code obfusqué n'est pas réversible

3. **Tester l'obfuscation** : Toujours tester le code obfusqué avant la distribution pour s'assurer qu'il fonctionne correctement

4. **Licence PyArmor** : La version gratuite affiche "trial" dans les fichiers obfusqués. Pour un usage commercial, consultez les licences PyArmor

## Réobfuscation

Pour mettre à jour le code obfusqué après des modifications :

```bash
# Supprimer l'ancien code obfusqué
rm -rf dist/

# Réobfusquer
pyarmor gen --recursive utils
```

## Commandes utiles

```bash
# Obfusquer un seul fichier
pyarmor gen module.py

# Obfusquer plusieurs dossiers
pyarmor gen --recursive utils models controllers

# Spécifier un dossier de sortie personnalisé
pyarmor gen --output build/obfuscated --recursive utils

# Obtenir de l'aide
pyarmor gen --help
```

## Ressources

- Documentation officielle : https://pyarmor.readthedocs.io/
- GitHub : https://github.com/dashingsoft/pyarmor

---
#### Auteur
**Hugo NGUYEN**: hugo.nguyen@credit-agricole-sa.fr