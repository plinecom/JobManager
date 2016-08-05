from jsonpath_rw import jsonpath, parse

__author__ = 'Masataka'


class JobInfoList:
    def __init__(self):
        self.current_job_id = -1
        self.jobList = []

    def get_current_job(self):
        if len(self.jobList) > 0:
            return self.jobList[self.current_job_id]

    def get_job_list(self):
        return self.jobList

    def set_current_job_id(self, job_id):
        if len(self.jobList) > job_id:
            self.current_job_id = job_id
        else:
            self.current_job_id = -1


class JobInfo:
    def __init__(self, param=None, dispatcher_list=None, config_info=None):
        # interface.IJob.__init__(self)
        self.test = 1

        self._param = []
        self._param.append({"job_setting_override": {
            "dispatcherIndex": 0  # GUI Select
        }})
        self._param.append({"configInfo": config_info})
        self._param.append({"fileInfo": param})
        self._param.append({"dispatcherInfo": dispatcher_list})

        self._param_key_list = {"job_setting_override": 0, "configInfo": 1, "fileInfo": 2, "dispatcherInfo": 3}
        # for paramKey in self._param_key_list:
#            self._param["job_setting_override"][0][paramKey] = 0

#        print "inst"
#        print self._param
#        print json.dumps(self._param, sort_keys=False, indent=4)
#        print self

    def setvalue(self, key, value):

        self._param[0]["job_setting_override"][key] = value
        # print json.dumps(self._param, sort_keys=False, indent=4)

    def getvalue(self, key):
        jsonpath_expr = parse(key)
        ret = [match.value for match in jsonpath_expr.find(self._param)]
        if len(ret) <= 0:
            ret = [""]
        return ret

    def get_jobname(self):
        template = self.getvalue("[*].configInfo.[*].*.jobNameTemplate")[0]
        job_name = template.replace("<filename>", self.getvalue("[*].*.fileNameWithoutExt")[0])
        return job_name
