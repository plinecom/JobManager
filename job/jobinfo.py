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
    def __init__(self, param=None, dispatcher=None, config=None):
#        interface.IJob.__init__(self)
        self.test=1

        self._param ={}
        self._param["fileInfo"] = param  # copy param Dictionary
        self._param["dispatcherInfo"] = dispatcher
        self._param["configInfo"] = config
        self._param["job_setting_override"] = {
            "dispatcher": 0
        }  # GUI Select
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
        self._param[key]["job_setting_override"]=value

    def getValue(self, key):

        category = None
        if self._param.has_key("job_setting_override"):
            category = "job_setting_override"
        elif self._param.has_key("configInfo"):
            category = "configInfo"
        elif self._param.has_key("job_setting_override"):
            category = "job_setting_override"
        elif self._param.has_key("dispatcherInfo"):
            category = "dispatcherInfo"
        else:
            return ""

        if category == "dispatcherInfo":
            if self._param[category][ self._param["job_setting_override"]].has_key(key):
                return self._param[category][ self._param["job_setting_override"]][key]
        elif self._param[category].has_key(key):
            return self._param[category][key]
        return ""
