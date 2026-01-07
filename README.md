# 🕒 Projet : L'Horloge de Mamie Jeannine

Bienvenue dans le projet **Clock**, développé avec amour pour Mamie Jeannine ! Ce programme en Python simule une horloge interactive permettant de régler l'heure, de configurer une alarme et de gérer différents modes d'affichage.

## 📖 Le Contexte
Après qu'un vilain chat a fait tomber l'horloge préférée de Mamie Jeannine, notre équipe de trois développeurs a décidé de mettre ses talents à profit pour lui coder une horloge sur mesure. Ce projet a été réalisé dans le cadre de notre formation en développement.

## 👥 L'Équipe
* **Mahira** : Architecture du moteur de temps et logique de boucle unique.
* **Moana** : Gestion des modes d'affichage (12h/24h) et système de pause.
* **Elyes** : Interaction utilisateur, gestion sécurisée des exceptions et documentation.

---

## 🚀 Fonctionnalités

### ✅ Fonctionnalités Obligatoires
* **Affichage en temps réel** : Horloge tournante au format `hh:mm:ss`.
* **Réglage de l'heure** : Fonction `afficher_heure(tuple)` permettant de modifier l'heure actuelle.
* **Système d'Alarme** : Fonction `set_alarm(tuple)` qui déclenche un message visuel lorsque l'heure choisie est atteinte.

### ✨ Bonus Implémentés
* **Mode 12h / 24h** : Basculez entre le format européen et le format AM/PM.
* **Arrêter le Temps (Pause)** : Fonction permettant de figer l'horloge pour faire des farces à Mamie.
* **Interface Réactive** : Utilisation de la bibliothèque `keyboard` pour une interaction fluide sans bloquer le programme.

---

## 🛠️ Installation et Lancement

### Prérequis
* Python 3.10 ou supérieur.
* Bibliothèque `keyboard` (nécessite les droits administrateur sur certains OS).

### Installation
1. Clonez le repository :
   ```bash
   git clone [https://github.com/votre-username/clock.git](https://github.com/votre-username/clock.git)

   cd clock

   pip install keyboard

   python projet perso.py

### Gestion des Erreurs et Exceptions

Conformément aux exigences pédagogiques, le projet intègre une gestion rigoureuse des entrées utilisateur :

ValueError : Capturée si l'utilisateur saisit du texte au lieu d'un nombre dans le menu ou les réglages.

Validation des données : Le programme vérifie que les heures sont entre 0-23, les minutes et secondes entre 0-59. Un message d'erreur précis est renvoyé en cas de valeur incohérente.

Prévention des plantages : Utilisation de blocs try...except autour des entrées input() pour garantir la stabilité du programme.

🔧 Choix Techniques
Pour résoudre le bug de mise à jour de l'heure et la réactivité de la touche "X", nous avons opté pour une boucle principale unique (Main Loop).

Cette architecture permet :

D'actualiser l'affichage même après une modification de l'heure.

De vérifier l'alarme en arrière-plan sans interrompre l'horloge.

D'écouter les touches du clavier de manière asynchrone sans que l'utilisateur ait besoin de rester appuyé sur la touche.

📅 Journal de bord
Gestion de projet : Suivi des tâches via le tableau Kanban sur GitHub Projects.

Branches : Utilisation d'un workflow par branche (feature/) pour chaque fonctionnalité.
