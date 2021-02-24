#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from importlib import import_module

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		pass

	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		pass
	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		pass
