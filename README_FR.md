# PgU1

Une voiture téléguidée construite à l'aide d'un Raspberry pi et d'un Arduino.

## Objectif

l'objectif est de concevoir une voiture téléguidée qui peut être contrôlée par un ordinateur
et qui peut patrouiller une pièce.

Afin de se localiser dans l'espace elle est munie d'une caméra et d'un pointeur laser. Ces deux outils conjointement avec openCv (python) 
servent de capteur de vitesse et de distance. L'analyse des données est gérée par un ordinateur lié
pas SSH au Rapsberry pi à l'aide de la librairie paramiko. 

Le robot est capable de prendre des photos et des vidéos et de les stocker dans la mémoire interne du Rapsberry pi
. Il est aussi capable de transférer ces fichiers dans l'ordinateur hôte.

La voiture est modélisée à l'aide du logiciel Creo Parametric 2.0 et est imprimée en 3D.

## Fonctionnement 

Le Raspberry pi est le coeur de la machine. Il commande la caméra, le laser, le mouvement du robot et la mémoire interne.
Celui-ci est connecté à un Arduino qui exécute les commandes du Rapsberry pi sur les moteurs et le laser à l'aide du port série. L'ordinateur
s'occupe de l'analyse des données et envoie des commandes au Rapsberry pi à distance.

Ordinateur ->Raspberry pi ->Arduino->composante de la machine

![alt text](https://github.com/featTheB/CAD-pgU1/blob/master/pdf_3d/assembly.jpg)

## Répertoire associé

Le code de l'ordinateur : https://github.com/featTheB/client_pgU1

La modélisation solide : https://github.com/featTheB/CAD-pgU1

## vidéo démo
capteur laser : https://youtu.be/xnBF-KOUick

matrice de localisation : https://youtu.be/wZwgmBapSVI
