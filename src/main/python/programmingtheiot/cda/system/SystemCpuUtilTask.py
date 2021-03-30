import logging
import psutil

from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask
from programmingtheiot.common import ConfigConst


class SystemCpuUtilTask(BaseSystemUtilTask):
	def __init__(self):
		super(SystemCpuUtilTask, self).__init__(name=ConfigConst.CPU_UTIL_NAME, typeID=ConfigConst.CPU_UTIL_TYPE)

	def _getSystemUtil(self):
		return psutil.cpu_percent()
