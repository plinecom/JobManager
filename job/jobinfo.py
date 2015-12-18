import interface

__author__ = 'Masataka'


class JobInfo():
    def __init__(self, param=None, dispatcher=None, config=None):
#        interface.IJob.__init__(self)
        self.test=1

        self._param ={}
        self._param["fileInfo"] = param  # copy param Dictionary
        self._param["dispatcherInfo"] = dispatcher
        self._param["configInfo"] = config
        self._param["job_setting_override"] = {}  # GUI Select
        print "inst"
        print self._param
        print self

    def getparam(self):
        return self._param

    def setValue(self, key, value):
        self._param[key]=value

    def getValue(self, key):

        if self._param.has_key(key):
            return self._param[key]
        return ""