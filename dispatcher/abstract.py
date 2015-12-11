import interface

class DispatcherBase(interface.IDispatcher):
    def __init__(self):
        interface.IDispatcher.__init__(self)
        self._param={}
        self._job=[]

    def setValue(self, key, value):
        self._param[key]=value

    def getValue(self, key):

        if self._param.has_key(key):
            return self._param[key]
        return ""
