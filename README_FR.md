# PgU1
Code dans le rapsberry pi de la voiture téléguidé

##Objectif

l'objectif est de faire une voiture téléguidé qui peut être controlé par un ordinateur
et qui peut patrouillé une pièce

Afin de se localisé dans l'espace elle est munis d'une camera et d'un pointeur laser. Ces deux outils conjointement avec openCv (python) 
servent de capteur de vitesse et de distance. L'analyse de donné sera géré par un ordinateur liée
pas SSH au rapsberry pi à l'aide de la librairie paramiko.

Le robot est capable de prendre des videos et des photos et de les stocker dans la mémoire interne du rapsberry pi
. Il est aussi capable ces fichiers dans l'ordinateur hôte.

##Fonctionnement 

Le rapsberry pi est le coeur de la machine. Il commande la camera,le laser, le mouvement du robot et la mémoire interne.
Celui-ci est connecté à un arduino exécutes les commandes du rapsberry pi sur les moteurs et le laser.L'ordinateur lui
commande s'occupe de l'analyse des images et envoie des commandes au rapsberry pi à distance.

Ordinateur ->Raspberry pi ->arduino->composante de la machine
