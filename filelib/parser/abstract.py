import os
import interface

__author__ = 'Masataka'


class FileParserBase(interface.IFileParser):
    def __init__(self, filepath):
        interface.IFileParser.__init__(self)
        self._param = {}
        self.setFilePath(filepath)
        self._param["batchframe"] = "0"
#        self._param["chunksize"] = studioPlugin.getDefaultChunksize()
#        self._param["machineLimit"] = studioPlugin.getDefaultMachineLimit()

    def getparam(self):
        return self._param

    def setFilePath(self, filePath):
        self._param["filePath"] = filePath
        self._param["job"] = os.path.splitext(os.path.basename(filePath))[0]
        self._param["proj"] = os.path.dirname(filePath)

    def getFilePath(self):
        return self._param["filePath"]

    def parse_preprocess(self):
        pass
#        scene = self.getFilePath();
#        projectPath = os.path.dirname(self.getFilePath())
#        projectName = self._studioPlugin.getProjectFromPath(self.getFilePath());

    def parse_process(self):
        pass

    def parse(self):
        print "test2"

        self.parse_preprocess()

        self.parse_process()
