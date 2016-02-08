from PyQt4 import QtGui, QtCore


class MayaPanel(QtGui.QWidget):

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

        self.app_combo.clear()
        itemListDic = {}
        tmp = self._jobList.get_current_job().getValue("Maya_executable")
        if isinstance(tmp,dict):
            itemListDic = tmp

        app_item_list = sorted(itemListDic.keys())
        self.app_combo.addItems(app_item_list)
        if self._jobList.get_current_job().getValue("application") in app_item_list:
            self.app_combo.setCurrentIndex(app_item_list.index(self._jobList.get_current_job().getValue("application")))
        self.app_combo.activated.connect(self.app_combo_activated)

        self.renderer_combo.clear()
        itemListDic = {}
        tmp = self._jobList.get_current_job().getValue("Maya_renderer")
        if isinstance(tmp,dict):
            itemListDic = tmp
        renderer_item_list = itemListDic.keys()
        self.renderer_combo.addItems(renderer_item_list)
#        print renderer_item_list
#        print self._jobList.get_current_job().getValue("renderer")
        if self._jobList.get_current_job().getValue("renderer") in renderer_item_list:
            self.renderer_combo.setCurrentIndex(renderer_item_list.index(self._jobList.get_current_job().getValue("renderer")))

    def app_combo_activated(self,index):
#        print index
        self._jobList.get_current_job().setValue("application", self.app_combo.currentText())
#        print self._jobList.get_current_job().getValue("application")