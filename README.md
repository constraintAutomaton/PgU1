# PgU1
The raspberry pi code of an RC car whit a camera

## Objectif
The objectif is to make a RC car that can be control via a computer and that can patrol a room.

It use a laser and a camera to locate the car in the space.The laser and camera will be used as a speed and distance captor using openCv (python).The computer will handle the video analysis.

The machine will be able to take video and photo and stock it in the pi intern memory and transfer those 
files to the computer.
## Operation
The raspberry pi will be the core of the machine. It command the camera, the movement module and the 
intern memory. The pi is connected to an arduino that execute the command to the motors and laser using the serial port. The computer send command to the pi accordingly to the user and do the video analysis. 

Computer -> Pi -> arduino

The RC car will be design using Creo parametric 2.0 and printed in 3d.
