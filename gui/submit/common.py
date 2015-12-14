from PyQt4 import QtGui, QtCore


class CommonPanel(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.init_ui()

    def init_ui(self):
        self.jobname_label = QtGui.QLabel("job name")
        self.jobname_qle = QtGui.QLineEdit(self)
        layout = QtGui.QGridLayout()
        layout.addWidget(self.jobname_label, 0, 0)
        layout.addWidget(self.jobname_qle, 0, 1)

        self.setLayout(layout)