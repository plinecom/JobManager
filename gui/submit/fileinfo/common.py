from PyQt4 import QtGui, QtCore


class CommonPanel(QtGui.QWidget):

    def __init__(self, job_list, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._jobList= job_list
        self.init_ui()

    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()
        self.jobname_label = QtGui.QLabel("job name")
        # print "tess"
        # print self._jobList.get_current_job().get_jobname()
        self.jobname_qle = QtGui.QLineEdit(self._jobList.get_current_job().get_jobname())
        self.jobname_qle.setReadOnly(True)

        layout.addWidget(self.jobname_label, height, 0)
        layout.addWidget(self.jobname_qle, height, 1)

        height += 1

        self.jobname_template_label = QtGui.QLabel("name template")
        # print "eee"
        # print self._jobList.get_current_job().getvalue("[*].configInfo.[*].*.jobNameTemplate")[0]
        self.jobname_template_qle = QtGui.QLineEdit(self._jobList.get_current_job().getvalue("[*].configInfo.[*].*.jobNameTemplate")[0])

        layout.addWidget(self.jobname_template_label, height, 0)
        layout.addWidget(self.jobname_template_qle, height, 1)

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
        self.start_frame_qle.textChanged.connect(self.start_frame_text_changed)
        layout.addWidget(self.start_frame_label, height, 0)
        layout.addWidget(self.start_frame_qle, height, 1)

        height += 1

        self.end_frame_label = QtGui.QLabel("end frame")
        self.end_frame_qle = QtGui.QLineEdit(self)
        self.end_frame_qle.textChanged.connect(self.end_frame_text_changed)
        layout.addWidget(self.end_frame_label, height, 0)
        layout.addWidget(self.end_frame_qle, height, 1)

        height += 1

        self.manager_label = QtGui.QLabel("manager")
        self.manager_combo = QtGui.QComboBox(self)
        layout.addWidget(self.manager_label, height, 0)
        layout.addWidget(self.manager_combo, height, 1)

        height += 1

        self.project_label = QtGui.QLabel("project")
        self.project_combo = QtGui.QComboBox(self)
        layout.addWidget(self.project_label, height, 0)
        layout.addWidget(self.project_combo, height, 1)

        height += 1

        self.setLayout(layout)

        self.update_ui()

    def update_ui(self):
        self.jobname_qle.setText(self._jobList.get_current_job().get_jobname())
        # print "id " + str(self._jobList.current_job_id)
        # print self._jobList.get_current_job().getvalue("jobName")
#        print self._jobList.get_current_job()._param
        # print "testz"
        # print self._jobList.get_current_job().getvalue("[*].fileInfo.endFrame")[0]
        self.end_frame_qle.setText(self._jobList.get_current_job().getvalue("[*].fileInfo.endFrame")[0])
        self.start_frame_qle.setText(self._jobList.get_current_job().getvalue("[*].fileInfo.startFrame")[0])

#        print self._jobList.get_current_job().getvalue("dispatch_software")
        self.manager_combo.addItems(["Qube6"])

    def start_frame_text_changed(self, text):
        print text
#       self._jobList.get_current_job().setvalue("startFrame", str(self.start_frame_qle.text()))

    def end_frame_text_changed(self, text):
        print text
#        self._jobList.get_current_job().setvalue("endFrame", str(self.end_frame_qle.text()))

    def group_item_selection_changed(self):
        item_list = []
        for item in self.group_listWidget.selectedItems():
            item_list.append(str(item.text()))
        # print item_list
        self._jobList.get_current_job().setvalue("selected_groups", item_list)
