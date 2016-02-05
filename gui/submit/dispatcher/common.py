from PyQt4 import QtGui, QtCore


class CommonPanel(QtGui.QWidget):

    def __init__(self,jobList, dispatcherList,configInfo, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._parent = parent
        self._joblist = jobList
        self._dipatcherList = dispatcherList
        self._configInfo = configInfo
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
        self.group_listWidget.addItems(self._dipatcherList[0]["groups"])

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

    def update_ui(self):



        self.priority_qle.setText(self._joblist.get_current_job().getValue("priority"))



#        print self._jobList.get_current_job().getValue("dispatch_software")


    def app_combo_activated(self,index):
#        print index
        self._jobList.get_current_job().setValue("application", self.app_combo.currentText())
#        print self._jobList.get_current_job().getValue("application")
    def start_frame_textChanged(self,text):
        print text
        self._jobList.get_current_job().setValue("startFrame", str(self.start_frame_qle.text()))
    def end_frame_textChanged(self,text):
        print text
        self._jobList.get_current_job().setValue("endFrame", str(self.end_frame_qle.text()))
    def group_itemSelectionChanged(self):
        itemList =[]
        for item in self.group_listWidget.selectedItems():
            itemList.append(str(item.text()))
        print itemList
        self._joblist.get_current_job().setValue("selected_groups", itemList)