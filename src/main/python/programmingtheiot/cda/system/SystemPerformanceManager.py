import logging

from apscheduler.schedulers.background import BackgroundScheduler

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask


class SystemPerformanceManager(object):

	def __init__(self):
		configUtil = ConfigUtil()

		self.cpuUtilPct = None
		self.memUtilPct = None

		self.pollRate = configUtil.getInteger(
			section=ConfigConst.CONSTRAINED_DEVICE,
			key=ConfigConst.POLL_CYCLES_KEY,
			defaultVal=ConfigConst.DEFAULT_POLL_CYCLES)
		self.locationID = configUtil.getProperty(
			section=ConfigConst.CONSTRAINED_DEVICE,
			key=ConfigConst.DEVICE_LOCATION_ID_KEY,
			defaultVal=ConfigConst.NOT_SET)

		if self.pollRate <= 0:
			self.pollRate = ConfigConst.DEFAULT_POLL_CYCLES

		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry(), 'interval', seconds=self.pollRate)

		self.cpuUtilTask = SystemCpuUtilTask()
		self.memUtilTask = SystemMemUtilTask()

		self.dataMsgListener = None
		# self.memUtilPct = None
		# self.cpuUtilPct = None

		logging.info("Initializing SystemPerformance Manager...")

	def handleTelemetry(self):
		self.cpuUtilPct = self.cpuUtilTask.getTelemetryValue()
		self.memUtilPct = self.memUtilTask.getTelemetryValue()
		logging.info('CPU utilization is %s percent, and memory utilization is %s percent.', str(self.cpuUtilPct), str(self.memUtilPct))

	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		pass

	def startManager(self):
		logging.info("Started SystemPerformanceManger.")

		if not self.scheduler.running:
			self.scheduler.start()
		else:
			logging.warning("SystemPerformanceManager scheduler already started. Ignoring.")

	def stopManager(self):
		logging.info("Stopped SystemPerformanceManger.")

		try:
			self.scheduler.shutdown()
		except:
			logging.warning("SystemPerformanceManager scheduler already stopped. Ignoring.")
