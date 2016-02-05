from PyQt4 import QtGui, QtCore


class JobListView(QtGui.QTreeWidget):

    def __init__(self,jobList, dispatcherList,configInfo, parent=None):
        QtGui.QListWidget.__init__(self, parent)
        self._parent = parent
        self._joblist = jobList
        self._dipatcherList = dispatcherList
        self._configInfo = configInfo
        self.update_ui()

    def update_ui(self):
        self.setColumnCount(2)
        self.clear()
        for jobinfo in self._joblist.get_joblist():
            item = QtGui.QTreeWidgetItem()
            item.setData(0,QtCore.Qt.DisplayRole,jobinfo.getValue("jobName"))
            self.addTopLevelItem(item)
