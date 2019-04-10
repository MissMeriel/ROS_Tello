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
	TransferringControl = 11

class WarningState(Enum):
	Default = 0
	LosingVicon = 1
	NoVicon = 2
	LowBattery = 3
	AbortingMission = 4

class MissionState(Enum):
	Default = 0
	FinishedBehavior = 1	#done sweeping
	Complete = 2	#back at home base
	WaitingForUser = 3 #can be handled by "Suspended"
	InProgress = 4	#sweeping or in manual mode
	InsideSweepArea = 5 #reached sweep area
	OutsideSweepArea = 6 #approaching sweep area
	Suspended = 7 #loss of vicon
	PossibleTargetDetected = 8
	Abort = 9 #emergency land

class UserState(Enum):
	Default = 0
	WatchingDrone = 1
	WatchingScreen = 2
	Fatigued = 3

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

class CommandState(Enum):
	Default = 0
	Auto = 1
	Manual = 2

class VelocityState(Enum):
	Default = 0
	Slow = 1
	Medium = 2
	Fast = 3

class BatteryState(Enum):
	Default = 0
	Low = 1
	Acceptable =  2
	High = 3
