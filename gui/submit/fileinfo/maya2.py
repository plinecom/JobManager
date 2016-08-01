from PyQt4 import QtGui, QtCore


class MayaPanel(QtGui.QWidget):

    def __init__(self, jobList, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._jobList= jobList
        self.init_ui()

    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()
        self.jobname_label = QtGui.QLabel("job name")
        self.jobname_qle = QtGui.QLineEdit(self._jobList.get_current_job().get_jobname())
        self.jobname_qle.setReadOnly(True)

        layout.addWidget(self.jobname_label, height, 0)
        layout.addWidget(self.jobname_qle, height, 1)

        height += 1

        self.renderer_proj_path_label = QtGui.QLabel("project path")
        self.renderer_proj_path_qle = QtGui.QLineEdit(self._jobList.get_current_job().getValue("proj")[0])

        layout.addWidget(self.renderer_proj_path_label, height, 0)
        layout.addWidget(self.renderer_proj_path_qle, height, 1)

        height += 1

        self.renderer_opt_label = QtGui.QLabel("other option")
        self.renderer_opt_qle = QtGui.QLineEdit()

        layout.addWidget(self.renderer_opt_label, height, 0)
        layout.addWidget(self.renderer_opt_qle, height, 1)

        height += 1

        self.setLayout(layout)
        self.update_ui()

    def update_ui(self):
        pass

    def app_combo_activated(self,index):
        # print index
        self._jobList.get_current_job().setValue("application", self.app_combo.currentText())
        # print self._jobList.get_current_job().getValue("application")
