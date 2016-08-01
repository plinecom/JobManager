import os
import platform
import json
import os.path


class AutoConfig:
    def __init__(self):

        self._param = {"auto_config": {}}

        system = platform.system()  # Windows, Linux, Darwin
        if "Darwin" in system:
            system = "MacOS_X"
        self._param["auto_config"]["system"] = system

        pathList =[]

        if "Windows" in system:
            pathList = ( os.environ['PATH'].split(';') )
        else:
            pathList = os.environ['PATH'].split(':')

        # print pathList
        script_dir_path = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(script_dir_path,"autoconf.json")
        config_file = open(config_path,'r')
        config = json.load(config_file)

        # search dispatcher

        self._param["auto_config"]["dispatcher"] = {}
        for dispatcher_name in config["dispatcher"].keys():
            if dispatcher_name == "localbatch":
                self._param["auto_config"]["dispatcher"][dispatcher_name] = config["dispatcher"][dispatcher_name]
                continue
#            print "test"
#            print  config[dispatcher_name]["submitter"][system].replace('\\\\','\\')
            submit_path =  config["dispatcher"][dispatcher_name]["submitter"][system].replace('\\\\', '\\')
            if os.path.exists(submit_path):
                self._param["auto_config"]["dispatcher"][dispatcher_name] = {}
                for param_key in config["dispatcher"][dispatcher_name].keys():
                    self._param["auto_config"]["dispatcher"][dispatcher_name][param_key] = config["dispatcher"][dispatcher_name][param_key][system].replace('\\\\', '\\')

                # print "path"

        # print self._param["auto_config"]["dispatcher"]
        # scan dispatcher typical point
        # scan dispatcher $PATH

        # scan registry  x too many times, too slow

        # search maya_executable

    def getparam(self):
        return self._param
