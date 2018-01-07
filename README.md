# PgU1
The raspberry pi code of an RC car whit a camera

## Goal
The objectif is to make a RC car that can be control via a computer and that can patrol a room.

It will use a laser and a camera to locate the car in the space.The laser will be used as a speed and distance captor using openCv.
The pi will not handle the video analysit it will be the computer.

The machine will be able to take video and photo and stock it in the pi and transfer those 
video and photo.

A raspberry pi will be the core of the machine. It will command the camera, the movement module and the 
intern memory. But the pi will not realy interact whit the real hardward it will be connected to an arduino 
that will do those operation. So the client will be the computer and the pi will be is server and the pi will 
be the client of the arduino. 

Computer -> Pi -> arduino

The RC car will be design using Creo parametric 2.0 and printed in 3d.
