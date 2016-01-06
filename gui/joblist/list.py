
class JobListView(QtGui.QWidget):

    def __init__(self, jobList, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._jobList= jobList
        self.init_ui()


    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()


        self.priority_label = QtGui.QLabel("priority")
        self.priority_qle = QtGui.QLineEdit(self)
        layout.addWidget(self.priority_label, height, 0)
        layout.addWidget(self.priority_qle, height, 1)

        height += 1


        self.group_label = QtGui.QLabel("group")
        self.group_listWidget = QtGui.QListWidget(self)
        self.group_listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.group_listWidget.addItems(self._jobList.get_current_job()._param["dispatcherInfo"][0]["groups"])
        self.group_listWidget.itemSelectionChanged.connect(self.group_itemSelectionChanged)
        # init selected
        items = self.group_listWidget.findItems("*",QtCore.Qt.MatchWildcard)
        for item in items:
            if "HP" in item.text():
                item.setSelected(True)
        layout.addWidget(self.group_label, height, 0)
        layout.addWidget(self.group_listWidget, height, 1)



        self.setLayout(layout)

        self.update_ui()