import logging
import psutil

from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask
from programmingtheiot.common import ConfigConst


class SystemMemUtilTask(BaseSystemUtilTask):
	def __init__(self):
		super(SystemMemUtilTask, self).__init__(name=ConfigConst.MEM_UTIL_NAME, typeID=ConfigConst.MEM_UTIL_TYPE)

	def _getSystemUtil(self):
		return psutil.virtual_memory().percent
