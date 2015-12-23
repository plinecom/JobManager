import os
import platform


class AutoConfig:
    def __init__(self):

        self._param = {}

        system = platform.system()
        if "Darwin" in system:
            system = "MacOS_X"
        self._param["system"] = system

        pathList =[]

        if "Windows" in system:
            pathList = ( os.environ['PATH'].split(';') )
        else:
            pathList = os.environ['PATH'].split(':')

        print pathList

        # scan dispatcher typical point
        # scan dispatcher $PATH

        #scan registry  x too many times, too slow

