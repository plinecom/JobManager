import interface

__author__ = 'Masataka'


class JobInfo(interface.IJob):
    def __init__(self,param, dispatcher=None, config=None):
        interface.IJob.__init__(self)

        self._param ={}
        self._param["fileInfo"] = param.copy()  # copy param Dictionary
        self._param["dispatcherInfo"] = dispatcher
        self._param["configInfo"] = config
        self._param["job_setting_override"] = {}  # GUI Select

    def getparam(self):
        return self._param

    def setValue(self, key, value):
        self._param[key]=value

    def getValue(self, key):

        if self._param.has_key(key):
            return self._param[key]
        return ""