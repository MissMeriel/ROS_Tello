#!/usr/bin/env python

from enum import Enum

class MissionState(Enum):
	Default = 0
	Complete = 1
	WaitingForUser = 2
	InProgress = 3
