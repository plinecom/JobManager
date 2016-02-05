from PyQt4 import QtGui, QtCore
import gui.submit.fileinfo.common
import gui.submit.fileinfo.maya


class FileinfoPanel(QtGui.QTabWidget):

    def __init__(self,jobList, dispatcherList,configInfo, parent=None):
        QtGui.QTabWidget.__init__(self)
        self._joblist = jobList
        print self._joblist.get_joblist()
        self._dipatcherList = dispatcherList
        self._configInfo = configInfo

        job_common_panel = gui.submit.fileinfo.common.CommonPanel(jobList, parent)
        maya_panel = gui.submit.fileinfo.maya.MayaPanel(jobList, parent)
        self.addTab(job_common_panel, "fileinfo")
        self.addTab(maya_panel, "Maya")
