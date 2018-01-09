# PgU1
RC Car build whit a Raspberry pi and an Arduino.

## Objectif
The objectif is to make a RC car that can be control via a computer and that can patrol a room.

It uses a laser and a camera to locate the car in the space.The laser and camera will be used as a speed and distance captor using openCv (python).The computer linked to the raspberry pi by SSH using the paramiko library will handle the video analysis.

The machine will be able to take video and photo and stock it in the pi intern memory and transfer those 
files to the computer.

The RC car will be design using Creo parametric 2.0 and printed in 3d.

## Operation
The Raspberry pi will be the core of the machine. It commands the camera, the movement module and the 
intern memory. The pi is connected to an Arduino that execute the command to the motors and laser using the serial port. The computer sends command to the pi accordingly to the user and do the video analysis. 

Computer -> Pi -> Arduino -> hardware

## Associate repository

The code for the computer side : https://github.com/featTheB/client_pgU1

The solid modelisation : https://github.com/featTheB/CAD-pgU1


