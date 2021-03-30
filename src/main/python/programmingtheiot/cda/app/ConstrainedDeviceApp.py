import logging

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

logging.basicConfig(format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)


class ConstrainedDeviceApp:
	"""
	Definition of the ConstrainedDeviceApp class.
	
	"""
	
	def __init__(self):
		"""
		Initialization of class.
		
		@param path The name of the resource to apply to the URI.
		"""
		logging.info("Initializing CDA...")
		self.sysPerfManager = SystemPerformanceManager()
		#self.pollRate = ConfigUtil.getInteger(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.POLL_CYCLES_KEY, ConfigConst.DEFAULT_POLL_CYCLES)

	def startApp(self):
		"""
		Start the CDA. Calls startManager() on the device data manager instance.
		
		"""
		logging.info("Starting CDA...")
		self.sysPerfManager.startManager()
		logging.info("CDA started.")

	def stopApp(self, code: int):
		"""
		Stop the CDA. Calls stopManager() on the device data manager instance.
		
		"""
		logging.info("CDA stopping...")
		self.sysPerfManager.stopManager()
		logging.info("CDA stopped with exit code %s.", str(code))
		
	def parseArgs(self, args):
		"""
		Parse command line args.
		
		@param args The arguments to parse.
		"""
		logging.info("Parsing command line args...")


def main():
	"""
	Main function definition for running client as application.
	
	Current implementation runs for 35 seconds then exits.
	"""
	cda = ConstrainedDeviceApp()
	cda.startApp()
	
	# run for 10 seconds - this can be changed as needed
	sleep(10)
	
	cda.stopApp(0)


if __name__ == '__main__':
	"""
	Attribute definition for when invoking as app via command line
	
	"""
	main()
