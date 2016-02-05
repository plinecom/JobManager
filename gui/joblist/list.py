from PyQt4 import QtGui, QtCore


class JobListView(QtGui.QListWidget):

    def __init__(self,jobList, dispatcherList,configInfo, parent=None):
        QtGui.QListWidget.__init__(self, parent)
        self._parent = parent
        self._joblist = jobList
        self._dipatcherList = dispatcherList
        self._configInfo = configInfo
        self.update_ui()

    def update_ui(self):
        self.clear()
        for jobinfo in self._joblist.get_joblist():
            self.addItem(jobinfo.getValue("jobName"))
