import interface

__author__ = 'Masataka'

class JobBase(interface.IJob):
    def __init__(self,param):
        interface.IJob.__init__(self)
        self._param ={}
        self._param["fileInfo"] = param.copy() #copy param Dictionary
        self._param["jobInfo"]={}

    def getparam(self):
        return self._param

    def setValue(self, key, value):
        self._param[key]=value

    def getValue(self, key):

        if self._param.has_key(key):
            return self._param[key]
        return ""