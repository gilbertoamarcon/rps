# rps
Relative Positioning System

This is a small python program to estimate relative robot positions from mutual distance measurements.
It takes in distances between robots and estimates their relative positions in the Cartesian plane.
To do so, it performs gradient descent on their relative distance equations.
It requires at least 5 robots to converge. 
A usage example code is provided in main.py.

Usage:
```
python main.py
```
