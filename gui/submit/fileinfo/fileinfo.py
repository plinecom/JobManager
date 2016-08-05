from PyQt4 import QtGui, QtCore
import gui.submit.fileinfo.common
import gui.submit.fileinfo.maya1
import gui.submit.fileinfo.maya2
import gui.submit.fileinfo.maya_mentalray


class FileinfoPanel(QtGui.QTabWidget):

    def __init__(self, jobList, dispatcherList, configInfo, parent=None):
        QtGui.QTabWidget.__init__(self)
        self._parent = parent
        self._joblist = jobList
        self._dipatcherList = dispatcherList
        self._configInfo = configInfo

        self.update_ui()

    def update_ui(self):
        self.clear()

        job_common_panel = gui.submit.fileinfo.common.CommonPanel(self._joblist, self._parent)
        self.addTab(job_common_panel, "fileinfo")

        if "Maya" in self._joblist.get_current_job().getvalue("[*].*.software")[0]:
            maya_panel1 = gui.submit.fileinfo.maya1.MayaPanel(self._joblist, self._parent)
            self.addTab(maya_panel1, "Maya1")
            maya_panel2 = gui.submit.fileinfo.maya2.MayaPanel(self._joblist, self._parent)
            self.addTab(maya_panel2, "Maya2")

            if "mentalray" in self._joblist.get_current_job().getvalue("[*].*.renderer")[0]:
                mentalray_panel = gui.submit.fileinfo.maya_mentalray.MentalrayPanel(self._joblist, self._parent)
                self.addTab(mentalray_panel, "Mentalray")
