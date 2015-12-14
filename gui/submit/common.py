from PyQt4 import QtGui, QtCore


class CommonPanel(QtGui.QWidget):

    def __init__(self, job, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._job= job
        self.init_ui()

    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()
        self.jobname_label = QtGui.QLabel("job name")
        self.jobname_qle = QtGui.QLineEdit(self._job._param["fileInfo"]["jobName"])

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
        self.app_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.app_label, height, 0)
        layout.addWidget(self.app_qle, height, 1)

        height += 1

        self.renderer_label = QtGui.QLabel("renderer")
        self.renderer_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.renderer_label, height, 0)
        layout.addWidget(self.renderer_qle, height, 1)

        height += 1

        self.group_label = QtGui.QLabel("group")
        self.group_combo = QtGui.QComboBox(self)
        self.group_combo.addItems(self._job._param["dispatcherInfo"][0].getparam()["groups"])
        layout.addWidget(self.group_label, height, 0)
        layout.addWidget(self.group_combo, height, 1)

        height += 1

        self.pool_label = QtGui.QLabel("pool/cluster")
        self.pool_combo = QtGui.QComboBox(self)
        self.pool_combo.addItems(self._job._param["dispatcherInfo"][0].getparam()["pools"])
        layout.addWidget(self.pool_label, height, 0)
        layout.addWidget(self.pool_combo, height, 1)

        self.setLayout(layout)