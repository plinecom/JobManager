import os
import platform
import json
import os.path

class AutoConfig:
    def __init__(self):

        self._param = {}

        system = platform.system() # Windows, Linux, Darwin
        if "Darwin" in system:
            system = "MacOS_X"
        self._param["system"] = system

        pathList =[]

        if "Windows" in system:
            pathList = ( os.environ['PATH'].split(';') )
        else:
            pathList = os.environ['PATH'].split(':')

        print pathList
        script_dir_path = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(script_dir_path,"autoconf.json")
        config_file = open(config_path,'r')
        config = json.load(config_file)

        self._param["dispatcher"] = {}
        for dispatcher_name in config.keys():
#            print "test"
#            print  config[dispatcher_name]["submitter"][system].replace('\\\\','\\')
            submit_path =  config[dispatcher_name]["submitter"][system].replace('\\\\','\\')
            if os.path.exists(submit_path):
                self._param["dispatcher"][dispatcher_name] = {}
                self._param["dispatcher"][dispatcher_name]["submitter"] = submit_path

                print "path"

        print self._param["dispatcher"]
        # scan dispatcher typical point
        # scan dispatcher $PATH

        #scan registry  x too many times, too slow

