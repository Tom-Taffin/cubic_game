# cubic_game

Un mini-jeu 2D développé avec **Pygame** en **programmation orientée objet**, où vous contrôlez un cube dans un environnement interactif avec des ennemis et des pièces à récupérer.  
Projet personnel visant à expérimenter les bases du développement de jeu avec Python.

## Démo

![Aperçu du jeu](demo/demo.gif)
![Aperçu d'un niveau du stage 1](demo/demo_stage1.gif)
![Aperçu d'un niveau du stage 2](demo/demo_stage2.gif)
![Aperçu d'un niveau du stage 3](demo/demo_stage3.gif)
![Aperçu d'un boss](demo/demo_boss.gif)
![Aperçu d'un niveau du stage 4](demo/demo_stage4.gif)
![Aperçu d'un niveau du stage 5](demo/demo_stage5.gif)

## Technologies utilisées

- Python 3
- [Pygame](https://www.pygame.org/)

---

## Installation & Lancement

1. **Cloner le projet**
```bash
git clone https://github.com/Tom-Taffin/cubic_game.git
cd cubic_game
```

2. **lancer le jeu**
```bash
python game.py
```

## Fonctionnalités

- Contrôle du cube via les touches directionnelles.
- Création de plusieurs types d’ennemis avec des comportements variés, dont des boss en forme de serpent qui poursuivent le joueur.
- Détection et gestion des collisions.
- Système de scènes avec navigation entre écrans (menu, jeu, défaite…).
- Création de boutons sélectionnables au clic ou au clavier.
- Création et gestion de niveaux progressifs.
- Sauvegarde des scores.
- Animation via enchaînement d’images.
- Gestion de la musique et des effets sonores.
- Timer intégré et parfois affiché sous forme de bar pour gérer le temps de jeu.
- Partitionnement de l’écran en tuiles, permettant la génération de labyrinthes dynamiques avec des murs mobiles.
- Implémentation de l’algorithme A* pour offrir à certains ennemis une navigation stratégique et intelligente dans le labyrinthe.


## Améliorations futures / en cours de développement

- Développement d'une **IA jouant au jeu via du Deep Q-Learning** pour expérimenter l’apprentissage par renforcement.
- Implémentation d’un **éditeur de niveaux** accessible depuis le menu du jeu.