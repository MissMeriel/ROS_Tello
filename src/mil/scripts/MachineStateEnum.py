#!/usr/bin/env python

from enum import Enum

class MachineState(Enum):
	Default = 0
	Hovering = 1
	Sweeping = 2
	GoToGoal = 3
	NoVicon = 4
	
