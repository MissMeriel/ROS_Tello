#!/usr/bin/env python

from enum import Enum

class MachineState(Enum):
	Default = 0
	Hovering = 1
	Sweeping = 2
	GoToGoal = 3
	NoVicon = 4
	

class MissionState(Enum):
	Default = 0
	Complete = 1
	WaitingForUser = 2
	InProgress = 3

class UserState(Enum):
	Default = 0
	WatchingDrone = 1
	WatchingScreen = 2
	#Fatigued = 3
