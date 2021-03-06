from PyQt4 import QtGui, QtCore


class QubePanel(QtGui.QWidget):

    def __init__(self, job_list, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._jobList= job_list
        self.init_ui()

    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()

        self.instance_num_label = QtGui.QLabel("instances")
        self.instance_num_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.instance_num_label, height, 0)
        layout.addWidget(self.instance_num_qle, height, 1)

        height += 1

        self.chunksize_label = QtGui.QLabel("chunksize")
        self.chunksize_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.chunksize_label, height, 0)
        layout.addWidget(self.chunksize_qle, height, 1)

        height += 1

        self.core_label = QtGui.QLabel("core")
        self.core_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.core_label, height, 0)
        layout.addWidget(self.core_qle, height, 1)

        height += 1

        self.coreall_label = QtGui.QLabel("core All(+)")
        self.coreall_qcb = QtGui.QCheckBox(self)
        layout.addWidget(self.coreall_label, height, 0)
        layout.addWidget(self.coreall_qcb, height, 1)

        height += 1

        self.pool_label = QtGui.QLabel("cluster")
        self.pool_combo = QtGui.QComboBox(self)
        # print "ccc"
        # print self._jobList.get_current_job().getvalue("[*].dispatcherInfo.[0].pools")
        self.pool_combo.addItems(self._jobList.get_current_job().getvalue("[*].dispatcherInfo.[0].pools")[0])
        layout.addWidget(self.pool_label, height, 0)
        layout.addWidget(self.pool_combo, height, 1)

        self.setLayout(layout)

        self.update_ui()

    def update_ui(self):

        self.core_qle.setText("8")

        # print self._jobList.get_current_job().getvalue("chunksize")
        self.chunksize_qle.setText(self._jobList.get_current_job().getvalue("chunksize")[0])

#        print self._jobList.get_current_job().getvalue("dispatch_software")

    def app_combo_activated(self, index):
        # print index
        self._jobList.get_current_job().setvalue("application", self.app_combo.currentText())
#        print self._jobList.get_current_job().getvalue("application")

    def start_frame_text_changed(self, text):
        # print text
        self._jobList.get_current_job().setvalue("startFrame", str(self.start_frame_qle.text()))

    def end_frame_text_changed(self, text):
        # print text
        self._jobList.get_current_job().setvalue("endFrame", str(self.end_frame_qle.text()))

    def group_item_selection_changed(self):
        item_list = []
        for item in self.group_listWidget.selectedItems():
            item_list.append(str(item.text()))
        print item_list
        self._jobList.get_current_job().setvalue("selected_groups", item_list)
