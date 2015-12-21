from PyQt4 import QtGui, QtCore


class CommonPanel(QtGui.QWidget):

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

        self.pj_path_label = QtGui.QLabel("proj path")
        self.pj_path_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.pj_path_label, height, 0)
        layout.addWidget(self.pj_path_qle, height, 1)

        height += 1

        self.scene_path_label = QtGui.QLabel("scene path")
        self.scene_path_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.scene_path_label, height, 0)
        layout.addWidget(self.scene_path_qle, height, 1)

        height += 1

        self.manager_label = QtGui.QLabel("manager")
        self.manager_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.manager_label, height, 0)
        layout.addWidget(self.manager_qle, height, 1)

        height += 1

        self.app_label = QtGui.QLabel("application")
        self.app_combo = QtGui.QComboBox(self)
        layout.addWidget(self.app_label, height, 0)
        layout.addWidget(self.app_combo, height, 1)

        height += 1

        self.renderer_label = QtGui.QLabel("renderer")
        self.renderer_combo = QtGui.QComboBox(self)
        layout.addWidget(self.renderer_label, height, 0)
        layout.addWidget(self.renderer_combo, height, 1)

        height += 1

        self.group_label = QtGui.QLabel("group")
        self.group_combo = QtGui.QComboBox(self)
        self.group_combo.addItems(self._jobList.get_current_job()._param["dispatcherInfo"][0]["groups"])
        layout.addWidget(self.group_label, height, 0)
        layout.addWidget(self.group_combo, height, 1)

        height += 1

        self.pool_label = QtGui.QLabel("pool/cluster")
        self.pool_combo = QtGui.QComboBox(self)
        self.pool_combo.addItems(self._jobList.get_current_job()._param["dispatcherInfo"][0]["pools"])
        layout.addWidget(self.pool_label, height, 0)
        layout.addWidget(self.pool_combo, height, 1)

        self.setLayout(layout)

        self.update_ui()

    def update_ui(self):
        self.jobname_qle.setText(self._jobList.get_current_job().getValue("jobName"))
        print self._jobList.get_current_job().getValue("jobName")
        print self._jobList.get_current_job()._param
        print "testz"
        self.app_combo.clear()

        app_item_list = sorted(self._jobList.get_current_job().getValue("Maya_executable").keys())
        self.app_combo.addItems(app_item_list)
        self.app_combo.setCurrentIndex(app_item_list.index(self._jobList.get_current_job().getValue("application")))