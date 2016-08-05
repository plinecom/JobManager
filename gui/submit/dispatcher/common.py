from PyQt4 import QtGui, QtCore


class CommonPanel(QtGui.QWidget):

    def __init__(self, job_list, dispatcher_list, config_info, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._parent = parent
        self._joblist = job_list
        self._dipatcherList = dispatcher_list
        self._configInfo = config_info
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
        self.group_listWidget.addItems(self._joblist.get_current_job().getvalue("[*].dispatcherInfo.[0].groups")[0])

        self.group_listWidget.itemSelectionChanged.connect(self.group_item_selection_changed)
        # init selected
        items = self.group_listWidget.findItems("*", QtCore.Qt.MatchWildcard)
        for item in items:
            if "HP" in item.text():
                item.setSelected(True)
        layout.addWidget(self.group_label, height, 0)
        layout.addWidget(self.group_listWidget, height, 1)

        self.setLayout(layout)

        self.update_ui()

    def update_ui(self):

        # print "priority"
        # print self._joblist.get_current_job().getvalue("[*].dispatcherInfo.[0].groups")
        self.priority_qle.setText(self._joblist.get_current_job().getvalue("[*].configInfo.[*].*.priority")[0])

        #  print self._jobList.get_current_job().getvalue("dispatch_software")

    def app_combo_activated(self, index):
        # print index
        self._jobList.get_current_job().setvalue("application", self.app_combo.currentText())
        # print self._jobList.get_current_job().getvalue("application")

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
        # print item_list
        self._joblist.get_current_job().setvalue("selected_groups", item_list)
