from PyQt4 import QtGui, QtCore


class MentalrayPanel(QtGui.QWidget):

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

        self.aml_label = QtGui.QLabel("auto mem limit")
        self.aml_qcb = QtGui.QCheckBox(self)
        layout.addWidget(self.aml_label, height, 0)
        layout.addWidget(self.aml_qcb, height, 1)

        height += 1

        self.mem_limit_label = QtGui.QLabel("memory limit(GB)")
        self.mem_limit__qle = QtGui.QLineEdit(self)
        layout.addWidget(self.mem_limit_label, height, 0)
        layout.addWidget(self.mem_limit__qle, height, 1)

        height += 1

        self.art_label = QtGui.QLabel("auto thread")
        self.art_qcb = QtGui.QCheckBox(self)
        layout.addWidget(self.art_label, height, 0)
        layout.addWidget(self.art_qcb, height, 1)

        height += 1

        self.thread_lim_label = QtGui.QLabel("thread limit")
        self.thread_lim_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.thread_lim_label, height, 0)
        layout.addWidget(self.thread_lim_qle, height, 1)

        height += 1

        self.setLayout(layout)
        self.update_ui()

    def update_ui(self):
        pass

    def app_combo_activated(self,index):
        # print index
        self._jobList.get_current_job().setValue("application", self.app_combo.currentText())
        # print self._jobList.get_current_job().getValue("application")
