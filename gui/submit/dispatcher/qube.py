from PyQt4 import QtGui, QtCore


class QubePanel(QtGui.QWidget):

    def __init__(self, jobList, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._jobList= jobList
        self.init_ui()


    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()

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

        self.pool_label = QtGui.QLabel("cluster")
        self.pool_combo = QtGui.QComboBox(self)
        self.pool_combo.addItems(self._jobList.get_current_job()._param["dispatcherInfo"][0]["pools"])
        layout.addWidget(self.pool_label, height, 0)
        layout.addWidget(self.pool_combo, height, 1)

        self.setLayout(layout)

        self.update_ui()

    def update_ui(self):

        self.core_qle.setText("8")

        print self._jobList.get_current_job().getValue("Maya_executable")

        app_item_list = sorted(self._jobList.get_current_job().getValue("Maya_executable").keys())

        print self._jobList.get_current_job().getValue("chunksize")
        self.chunksize_qle.setText(self._jobList.get_current_job().getValue("chunksize"))



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
        self._jobList.get_current_job().setValue("selected_groups", itemList)