from PyQt4 import QtGui, QtCore


class CommonPanel(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.init_ui()

    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()
        self.jobname_label = QtGui.QLabel("job name")
        self.jobname_qle = QtGui.QLineEdit(self)

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

        self.setLayout(layout)