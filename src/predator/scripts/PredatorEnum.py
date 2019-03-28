#!/usr/bin/env python

from enum import Enum

class MachineState(Enum):
	Default = 0
	Hovering = 1
	Sweeping = 2
	OutsideSweepArea = 3
	LosingVicon = 4
	NoVicon = 5
	PossibleTargetDetected = 6
	FinishedBehavior = 7
	Landing = 8
	Manual = 9
	LowBattery = 10
	TransferringControl = 11

class WarningState(Enum):
	Default = 0
	LosingVicon = 4
	NoVicon = 5
	LowBattery = 10

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

class UserCommand(Enum):
	Default = 0
	LookCloser = 1
	ReturnHome = 2
	KeepHovering = 3
	KeepSweeping = 4
	SweepAgain = 5
	Land = 6
	Left = 7
	Right = 9
	Up = 10
	Down = 11
	RequestAutoControl = 12
	RequestManualControl = 13
