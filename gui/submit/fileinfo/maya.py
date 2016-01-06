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
        self.jobname_qle = QtGui.QLineEdit(self._jobList.get_current_job().getValue("jobName"))

        layout.addWidget(self.jobname_label, height, 0)
        layout.addWidget(self.jobname_qle, height, 1)

        height += 1

        self.renderer_label = QtGui.QLabel("renderer")
        self.renderer_combo = QtGui.QComboBox(self)
        layout.addWidget(self.renderer_label, height, 0)
        layout.addWidget(self.renderer_combo, height, 1)

        height += 1
        self.setLayout(layout)
        self.update_ui()

    def update_ui(self):

        self.renderer_combo.clear()
        renderer_item_list = self._jobList.get_current_job().getValue("Maya_renderer").keys()
        self.renderer_combo.addItems(renderer_item_list)
#        print renderer_item_list
#        print self._jobList.get_current_job().getValue("renderer")
        if self._jobList.get_current_job().getValue("renderer") in renderer_item_list:
            self.renderer_combo.setCurrentIndex(renderer_item_list.index(self._jobList.get_current_job().getValue("renderer")))
