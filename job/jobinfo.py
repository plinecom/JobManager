import interface
import json
from jsonpath_rw import jsonpath, parse

__author__ = 'Masataka'

class JobInfoList():
    def __init__(self):
        self.current_job_id = -1
        self.jobList = []

    def get_current_job(self):
        if len(self.jobList) > 0:
            return self.jobList[self.current_job_id]
        else:
            return JobInfo()

    def get_joblist(self):
        return self.jobList

    def set_current_job_id(self,id):
        if len( self.jobList ) > id:
            self.current_job_id = id
        else:
            self.current_job_id = -1


class JobInfo():
    def __init__(self, param=None, dispatcherList=None, configInfo=None):
#        interface.IJob.__init__(self)
        self.test=1

        self._param =[]
        self._param.append({"job_setting_override":{
            "dispatcherIndex":0 # GUI Select
        }})
        if configInfo is not None:
            for config in configInfo._configlist:
                self._param.append(config)
        self._param.append({"fileInfo":param})
        self._param.append({"dispatcherInfo":dispatcherList})


        self._paramkeyList = ["job_setting_override", "configInfo", "fileInfo", "dispatcherInfo"]
 #       for paramKey in self._paramkeyList:
#            self._param["job_setting_override"][0][paramKey] = 0

        print "inst"
        print self._param
        print json.dumps(self._param, sort_keys=False, indent=4)
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

        self._param[0]["job_setting_override"][key] = value

        print json.dumps(self._param, sort_keys=False, indent=4)

    def getValue(self, key):
        jsonpath_expr = parse(key)
        ret =  [match.value for match in jsonpath_expr.find( self._param)]
        if len(ret) <= 0:
            ret = [""]
        return ret

        category = None
        for param_key in self._param:
            print param_key
            if param_key is not None:
                #print param_key
#                print self._param["job_setting_override"]
#                print self._param[param_key]
#                print self._param[param_key]
                if "configInfo" in param_key:
                   value = param_key["configInfo"].getvalue(key)
                   if value is not None:
                       return value
                elif "dispatcherInfo" in param_key:
                    print self._param[-1]["job_setting_override"]

                    if param_key[self._param[-1]["job_setting_override"]["dispatcherIndex"]].has_key(key):
                        return param_key[self._param[-1]["job_setting_override"]["dispatcherIndex"]][key]
                else:
                    if param_key.has_key(key):
                        return self._param[param_key][key]

        return ""
