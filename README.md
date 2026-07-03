# Bot Clicker

Solution d'automatisation pour le jeu "Cookie Clicker" — outil léger en Python conçu pour automatiser le clic sur le cookie principal de façon fiable et modulaire.

## Présentation

Bot Clicker simplifie les démonstrations et les tests en automatisant les interactions de base avec Cookie Clicker. Le projet privilégie la simplicité d'utilisation et la facilité d'extension.

## Fonctionnalités

- Clic automatique sur le cookie principal
- Interface graphique minimale (tkinter) pour visualiser l'état et afficher les commandes (raccourci : MAJ + X)
- Exécution multi‑threadée : interface et moteur d'automatisation séparés

## Prérequis

- Python 3.8 ou plus récent
- Dépendances listées dans le fichier `requirements.txt`

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/Suban97/Bot_Clicker.git
cd Bot_Clicker
```

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Démarrer l'application :

```bash
python main.py
```

Le bot s'exécute en tâche de fond et la fenêtre d'interface s'ouvre. Appuyez sur MAJ + X pour afficher ou masquer la fenêtre de commandes.

## Commandes

- Commande : MAJ + X — Afficher / masquer la fenêtre de commandes
- Commande : MAJ + W — Mettre le bot en pause / reprendre (toggle)
- Commande : MAJ + Q — Arrêter le bot et quitter l'application

> Remarque : les raccourcis ci‑dessus reflètent le comportement actuel du code (détection clavier dans `interne/Window.py` et contrôles dans `interne/Bot_Clicker.py`). Si tu veux modifier les raccourcis, je peux mettre à jour le code pour qu'ils correspondent.

## Structure du package

Arborescence principale (racine du dépôt) :

- README.md — documentation utilisateur (ce fichier)
- main.py — point d'entrée : démarre le thread du bot et lance l'interface
- requirements / requirements.txt — liste des dépendances pip requises
- interne/ — package d'implémentation
  - interne/Bot_Clicker.py — logique du bot
    - start_bot() : ouvre le navigateur sur Cookie Clicker, localise l'image `interne/ressources/Cookie.png` et effectue des clics au centre de la zone détectée ; gère la pause et l'arrêt
  - interne/Window.py — interface utilisateur (tkinter)
    - Win() : crée la fenêtre, affiche les commandes et démarre un thread de détection clavier pour MAJ + X
  - interne/ressources/Cookie.png — image utilisée par pyautogui pour la détection
  - interne/__pycache__/ — caches Python (ignorés pour la distribution)

## Remarques et limitations connues

- Détection du cookie :
  - Si la détection du cookie ne s'effectue pas automatiquement après le chargement de la page, essaie de dézoomer la page (Ctrl + - / Cmd + -) ; cela résout fréquemment les problèmes de repérage liés à l'échelle d'affichage.
  - Ce comportement est lié à la méthode actuelle de détection par image (sensibilité au zoom / DPI) ; une amélioration est prévue pour rendre la détection plus robuste.

---

