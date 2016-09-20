from PyQt4 import QtGui, QtCore


class NukePanel(QtGui.QWidget):
    def __init__(self, job_list, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._jobList = job_list
        self.init_ui()

    def init_ui(self):
        height = 0
        layout = QtGui.QGridLayout()
        self.jobname_label = QtGui.QLabel("job name")
        self.jobname_qle = QtGui.QLineEdit(self._jobList.get_current_job().get_jobname())
        self.jobname_qle.setReadOnly(True)

        layout.addWidget(self.jobname_label, height, 0)
        layout.addWidget(self.jobname_qle, height, 1)

        height += 1

        self.app_label = QtGui.QLabel("application")
        self.app_combo = QtGui.QComboBox(self)
        layout.addWidget(self.app_label, height, 0)
        layout.addWidget(self.app_combo, height, 1)

        height += 1

        self.camera_label = QtGui.QLabel("camera")
        self.camera_combo = QtGui.QComboBox(self)
        layout.addWidget(self.camera_label, height, 0)
        layout.addWidget(self.camera_combo, height, 1)

        height += 1

        self.layer_label = QtGui.QLabel("layer")
        self.layer_combo = QtGui.QComboBox(self)
        layout.addWidget(self.layer_label, height, 0)
        layout.addWidget(self.layer_combo, height, 1)

        height += 1

        self.renderer_label = QtGui.QLabel("renderer")
        self.renderer_combo = QtGui.QComboBox(self)
        layout.addWidget(self.renderer_label, height, 0)
        layout.addWidget(self.renderer_combo, height, 1)

        height += 1

        self.renderer_dir_label = QtGui.QLabel("output dir")
        self.renderer_dir_qle = QtGui.QLineEdit()

        layout.addWidget(self.renderer_dir_label, height, 0)
        layout.addWidget(self.renderer_dir_qle, height, 1)

        height += 1

        self.renderer_filetype_label = QtGui.QLabel("outfile name")
        self.renderer_filetype_qle = QtGui.QLineEdit()

        layout.addWidget(self.renderer_filetype_label, height, 0)
        layout.addWidget(self.renderer_filetype_qle, height, 1)

        height += 1

        self.setLayout(layout)
        self.update_ui()

    def update_ui(self):
        # print self._jobList.get_current_job().getvalue("[*].fileInfo")[0]
        self.layer_combo.clear()
        app_layer_list = self._jobList.get_current_job().getvalue("[*].fileInfo.render_layer_list")[0]
        # print app_layer_list
        app_layer_list.insert(0, "")
        self.layer_combo.addItems(app_layer_list)
        if self._jobList.get_current_job().getvalue("application") in app_layer_list:
            self.layer_combo.setCurrentIndex(
                app_layer_list.index(self._jobList.get_current_job().getvalue("application")))
        #        self.layer_combo.activated.connect(self.app_combo_activated)

        self.camera_combo.clear()

        camera_list = self._jobList.get_current_job().getvalue("[*].fileInfo.camera_list")[0]
        self.camera_combo.addItems(camera_list)
        if self._jobList.get_current_job().getvalue("application") in camera_list:
            self.camera_combo.setCurrentIndex(
                camera_list.index(self._jobList.get_current_job().getvalue("application")))
        #        self.camera_combo.activated.connect(self.app_combo_activated)

        self.app_combo.clear()
        item_list_dic = {}
        tmp = self._jobList.get_current_job().getvalue("[*].configInfo.[*].*.Nuke_executable")[0]
        # print "test"
        # print tmp
        if isinstance(tmp, dict):
            item_list_dic = tmp

        app_item_list = sorted(item_list_dic.keys())
        self.app_combo.addItems(app_item_list)
        if self._jobList.get_current_job().getvalue("[*].fileInfo.application")[0] in app_item_list:
            self.app_combo.setCurrentIndex(
                app_item_list.index(self._jobList.get_current_job().getvalue("[*].fileInfo.application")[0]))
        self.app_combo.activated.connect(self.app_combo_activated)

        self.renderer_combo.clear()
        item_list_dic = {}
        tmp = self._jobList.get_current_job().getvalue("[*].*.[*].*.Maya_renderer")[0]
        if isinstance(tmp, dict):
            item_list_dic = tmp
        renderer_item_list = item_list_dic.keys()
        self.renderer_combo.addItems(renderer_item_list)
        #        print renderer_item_list
        #        print self._jobList.get_current_job().getvalue("renderer")
        if self._jobList.get_current_job().getvalue("[*].fileInfo.renderer")[0] in renderer_item_list:
            self.renderer_combo.setCurrentIndex(
                renderer_item_list.index(self._jobList.get_current_job().getvalue("[*].fileInfo.renderer")[0]))

    def app_combo_activated(self, index):
        # print index
        self._jobList.get_current_job().setvalue("application", str(self.app_combo.currentText()))
        # print self._jobList.get_current_job().getvalue("application")
