from PyQt4 import QtGui, QtCore


class JobListView(QtGui.QTreeWidget):

    def __init__(self, jobList, dispatcherList, configInfo, parent=None):
        QtGui.QListWidget.__init__(self, parent)
        self._parent = parent
        self._joblist = jobList
        self._dipatcherList = dispatcherList
        self._configInfo = configInfo
        self.setSelectionMode(self.ExtendedSelection)
        self.currentItemChanged.connect(self.item_changed)

        self.update_ui()

    def update_ui(self):
        self.setColumnCount(2)
        self.clear()
        i = 0
        for jobinfo in self._joblist.get_joblist():
            item = QtGui.QTreeWidgetItem()
            item.setData(0, QtCore.Qt.DisplayRole, jobinfo.get_jobname())
            item.setData(0, QtCore.Qt.UserRole, i)
            self.addTopLevelItem(item)
            # print "index "+str(i)
            i += 1

    def item_changed(self, current_item, previous_item):

        if current_item is None:
            return

        # print current_item.text(0)
        jobid = current_item.data(0, QtCore.Qt.UserRole)
        i = 0
        for jobinfo in self._joblist.get_joblist():
            if jobid == i:
                self._joblist.set_current_job_id(i)
                print "hit"
                print i
                print self._joblist.current_job_id
                break
            i += 1
        parent = self.parent()
        while parent != 0:
            # print parent
            if parent.windowTitle() == "JobManager":
                parent.update_ui_right_pannel()
                break
            parent = parent.parent()
