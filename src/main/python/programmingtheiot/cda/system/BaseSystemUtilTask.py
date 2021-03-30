import programmingtheiot.common.ConfigConst as ConfigConst
import logging

from programmingtheiot.data.SensorData import SensorData

class BaseSystemUtilTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, sensorName=ConfigConst.NOT_SET):
		###
		# TODO: fill in the details here
		self.latestSensorData = None
		
		pass

	def __init__(self, name=ConfigConst.NOT_SET, typeID=ConfigConst.DEFAULT_SENSOR_TYPE):
		self.name = name
		self.typeID = typeID

	def getName(self):
		return self.name

	def getTypeID(self):
		return self.typeID

	def generateTelemetry(self) -> SensorData:
		###
		# TODO: fill in the details here
		#
		# NOTE: Use self._getSystemUtil() to retrieve the value from the sub-class
		pass
		
	def getTelemetryValue(self):
		val = self._getSystemUtil()
		logging.info(self.__class__.__name__, val)
		return val

	def getTelemetryValue(self) -> float:
		pass

	def _getSystemUtil(self) -> float:
		"""
		Template method implemented by sub-class.
		
		Retrieve the system utilization value as a float.
		
		@return float
		"""
		pass
