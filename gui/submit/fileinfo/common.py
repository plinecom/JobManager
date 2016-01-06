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

#        self.pj_path_label = QtGui.QLabel("proj path")
#        self.pj_path_qle = QtGui.QLineEdit(self)
#        layout.addWidget(self.pj_path_label, height, 0)
#        layout.addWidget(self.pj_path_qle, height, 1)

#        height += 1

#        self.scene_path_label = QtGui.QLabel("scene path")
#        self.scene_path_qle = QtGui.QLineEdit(self)
#        layout.addWidget(self.scene_path_label, height, 0)
#        layout.addWidget(self.scene_path_qle, height, 1)

#        height += 1

        self.start_frame_label = QtGui.QLabel("start frame")
        self.start_frame_qle = QtGui.QLineEdit(self)
        self.start_frame_qle.textChanged.connect(self.start_frame_textChanged)
        layout.addWidget(self.start_frame_label, height, 0)
        layout.addWidget(self.start_frame_qle, height, 1)

        height += 1

        self.end_frame_label = QtGui.QLabel("end frame")
        self.end_frame_qle = QtGui.QLineEdit(self)
        self.end_frame_qle.textChanged.connect(self.end_frame_textChanged)
        layout.addWidget(self.end_frame_label, height, 0)
        layout.addWidget(self.end_frame_qle, height, 1)

        height += 1

        self.manager_label = QtGui.QLabel("manager")
        self.manager_combo = QtGui.QComboBox(self)
        layout.addWidget(self.manager_label, height, 0)
        layout.addWidget(self.manager_combo, height, 1)

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

        self.setLayout(layout)

        self.update_ui()

    def update_ui(self):
        self.jobname_qle.setText(self._jobList.get_current_job().getValue("jobName"))
        print self._jobList.get_current_job().getValue("jobName")
#        print self._jobList.get_current_job()._param
#        print "testz"

        self.app_combo.clear()

        print self._jobList.get_current_job().getValue("Maya_executable")

        app_item_list = sorted(self._jobList.get_current_job().getValue("Maya_executable").keys())
        self.app_combo.addItems(app_item_list)
        if self._jobList.get_current_job().getValue("application") in app_item_list:
            self.app_combo.setCurrentIndex(app_item_list.index(self._jobList.get_current_job().getValue("application")))
        self.app_combo.activated.connect(self.app_combo_activated)

        self.renderer_combo.clear()
        renderer_item_list = self._jobList.get_current_job().getValue("Maya_renderer").keys()
        self.renderer_combo.addItems(renderer_item_list)
#        print renderer_item_list
#        print self._jobList.get_current_job().getValue("renderer")
        if self._jobList.get_current_job().getValue("renderer") in renderer_item_list:
            self.renderer_combo.setCurrentIndex(renderer_item_list.index(self._jobList.get_current_job().getValue("renderer")))


        self.start_frame_qle.setText(self._jobList.get_current_job().getValue("startFrame"))
        self.end_frame_qle.setText(self._jobList.get_current_job().getValue("endFrame"))
        print self._jobList.get_current_job().getValue("chunksize")



#        print self._jobList.get_current_job().getValue("dispatch_software")
        self.manager_combo.addItems(["Qube6"])

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