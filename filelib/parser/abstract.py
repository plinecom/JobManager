import os
import interface

__author__ = 'Masataka'


class FileParserBase(interface.IFileParser):
    def __init__(self, file_path):
        interface.IFileParser.__init__(self)
        self._param = {}
        self.set_file_path(file_path)
        self._param["batchframe"] = "0"
#        self._param["chunksize"] = studioPlugin.getDefaultChunksize()
#        self._param["machineLimit"] = studioPlugin.getDefaultMachineLimit()

    def getparam(self):
        return self._param

    def set_file_path(self, file_path):
        self._param["filePath"] = file_path
        self._param["fileNameWithoutExt"] = os.path.splitext(os.path.basename(file_path))[0]
        self._param["proj"] = os.path.dirname(file_path)

    def get_file_path(self):
        return self._param["filePath"]

    def parse_pre_process(self):
        pass
#        scene = self.get_file_path();
#        projectPath = os.path.dirname(self.get_file_path())
#        projectName = self._studioPlugin.getProjectFromPath(self.get_file_path());

    def parse_process(self):
        pass

    def parse(self):
        # type: () -> object
        # print "test2"

        self.parse_pre_process()

        self.parse_process()

        self._param["jobName"] = self._param["fileNameWithoutExt"]\
                                 + "_" + self._param["software"]\
                                 + "_" + self._param["renderer"]
