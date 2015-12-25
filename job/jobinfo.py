import interface


__author__ = 'Masataka'

class JobInfoList():
    def __init__(self):
        self.current_job_id = -1
        self.jobList = []

    def get_current_job(self):
        return self.jobList[self.current_job_id]

    def get_joblist(self):
        return self.jobList

    def set_current_job_id(self,id):
        if len( self.jobList ) < id:
            self.current_job_id = id
        else:
            self.current_job_id = -1


class JobInfo():
    def __init__(self, param=None, dispatcherList=None, configInfo=None):
#        interface.IJob.__init__(self)
        self.test=1

        self._param ={}
        self._param["fileInfo"] = param  # copy param Dictionary
        self._param["dispatcherInfo"] = dispatcherList
        self._param["configInfo"] = configInfo
        self._param["job_setting_override"] = {
            "dispatcherIndex":0
        }  # GUI Select
        self._paramkeyList = ["job_setting_override", "configInfo", "fileInfo", "dispatcherInfo"]
 #       for paramKey in self._paramkeyList:
#            self._param["job_setting_override"][0][paramKey] = 0

        print "inst"
        print self._param
        print self

    def getparam(self):
        return self._param

    def getlist_dispatcher(self):
        key = "dispatcherInfo"
        param = []
        if self._param.has_key(key):
            param = self._param["dispatcherInfo"]
        return param

    def getparam_config(self):
        key = "configInfo"
        param = {}
        if self._param.has_key(key):
            param = self._param["configInfo"]
        return param

    def setValue(self, key, value):
        self._param["job_setting_override"][key]=value

    def getValue(self, key):

        category = None
        for param_key in self._paramkeyList:
            if self._param.has_key(param_key):
                #print param_key
#                print self._param["job_setting_override"]
#                print self._param[param_key]
#                print self._param[param_key]
                if param_key == "configInfo":
                    value = self._param[param_key].getvalue(key)
                    if value is not None:
                        return value
                elif param_key == "dispatcherInfo":
                    if self._param[param_key][self._param["job_setting_override"]["dispatcherIndex"]].has_key(key):
                        return self._param[param_key][self._param["job_setting_override"]["dispatcherIndex"]][key]
                else:
                    if self._param[param_key].has_key(key):
                        return self._param[param_key][key]

        return ""
