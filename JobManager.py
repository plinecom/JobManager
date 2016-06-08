import os.path
import sys

import yaml
import json
from PyQt4 import QtGui, QtCore

import config.auto.autoconf
import config.config
import dispatcher.qube
import filelib.parser.lib
import gui.submit.dispatcher.common
import gui.submit.dispatcher.qube
import gui.submit.fileinfo.fileinfo
import gui.joblist.list
import job.jobinfo


class MainWindow(QtGui.QMainWindow):
    def __init__(self,jobList, dispatcherList,configInfo, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self._joblist = jobList
        print self._joblist.get_joblist()
        self._dipatcherList = dispatcherList
        self._configInfo = configInfo

        self.setAcceptDrops(True)
        panel = QtGui.QWidget()
        panel.setObjectName("commonPanel")

        #main_window.setAcceptDrops(True)

        fileinfo_tab = gui.submit.fileinfo.fileinfo.FileinfoPanel(jobList, dispatcherList,configInfo, panel)

        dispatcher_common_panel = gui.submit.dispatcher.common.CommonPanel(jobList, dispatcherList,configInfo, panel)
        qube_panel = gui.submit.dispatcher.qube.QubePanel(jobList, panel)
        qtabRLow = QtGui.QTabWidget()
        qtabRLow.addTab(dispatcher_common_panel, "dispatcher")
        qtabRLow.addTab(qube_panel, "Qube")


        panel_layout = QtGui.QVBoxLayout()
        panel_layout.addWidget(fileinfo_tab)
        panel_layout.addWidget(qtabRLow)

        button_submit =QtGui.QPushButton("sumbmit")
        button_submit.clicked.connect(self.on_button_submit)
        panel_layout.addWidget(button_submit)

        panel.setLayout(panel_layout)

        panelL = QtGui.QWidget()
        panelL.setObjectName("listPanel")

        #main_window.setAcceptDrops(True)


        qsplitV =QtGui.QSplitter(QtCore.Qt.Vertical)
        panelL_layout = QtGui.QVBoxLayout()
        qtabL = QtGui.QTabWidget()
        self._list_view = gui.joblist.list.JobListView(jobList, dispatcherList,configInfo, panel)

        qtabL.addTab( self._list_view, "Job")




        txtBrowser = QtGui.QTextBrowser()
        txtBrowser.append("test")
        qtabLLow = QtGui.QTabWidget()
        qtabLLow.addTab(txtBrowser, "console")

        qsplitV.addWidget(qtabL)
        qsplitV.addWidget(qtabLLow)

        panelL_layout.addWidget(qsplitV)

        panelL.setLayout(panelL_layout)

        qsplitH = QtGui.QSplitter(QtCore.Qt.Horizontal)



        qsplitH.addWidget(panelL)
        qsplitH.addWidget(panel)



        self.setWindowTitle("JobManager")
        self.setCentralWidget(qsplitH)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for u in event.mimeData().urls():
            print u.toLocalFile()
            file_parser = filelib.parser.lib.fileParse(str(u.toLocalFile()))
            print file_parser.getparam()
            self._joblist.get_joblist().append(
                    job.jobinfo.JobInfo(
                            file_parser.getparam(),
                            self._dipatcherList,
                            self._configInfo
                    )
            )

            print self._joblist.get_current_job()

        self._joblist.set_current_job_id(-1)
        self.update_ui()

    def update_ui(self):
#        common_panel = self.findChild(gui.submit.fileinfo.common.CommonPanel)
#        common_panel.update_ui()
        self.update_ui_right_pannel()
        self._list_view.update_ui()

    def update_ui_right_pannel(self):
        tab_panel = self.findChild(gui.submit.fileinfo.fileinfo.FileinfoPanel)
        tab_panel.update_ui()


    def on_button_submit(self):
        dispatcher = self._joblist.get_current_job().getValue("dispatherObj")
        dispatcher.submit(self._joblist.get_current_job())
        print "submit"



def loadFile(absPath):
    return job


if __name__ == "__main__":


    #addFilePath = "/root/test_maya_2015.mb"
    addFilePath = None

    if(len(sys.argv) > 1):
        addFilePath = sys.argv[1]


    auto_config = config.auto.autoconf.AutoConfig().getparam()


    script_dir_path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(script_dir_path,"config","config.yml")
    print config_path
    config_file = open(config_path,'r')
    config_data = yaml.load(config_file)

    config_data["00"] = auto_config
    print config
    configList=[]
    #configList.append(auto_config["dispatcher"])
    for key in sorted(config_data.keys(), reverse=True):
        configList.append(config_data[key])

    print configList
    print json.dumps(configList, sort_keys=False, indent=4)
    configInfo = config.config.ConfigInfo(configList)
#    print configInfo.getvalue("priority")
#    print configInfo.getvalue("priority")
    configInfo.getvalueJsonPath("[*].*.priority")
    print configInfo.getvalueJsonPath("[*].*.dispatcher")
    #command line mode?

    # loadFile(addFilePath)
    fileParam = {}
    if addFilePath is not None:
        fileParser = filelib.parser.lib.fileParse(addFilePath)
        print fileParser.getparam()
        fileParam = fileParser.getparam()
#
#    job_factory = jobfactory.factory.JobFactory()
#    job = job_factory.getJob(fileParser.getparam(), "SudioPlugin()")
    dispatcherList = []
    for dispatcher_info in  configInfo.getvalueJsonPath("[*].*.dispatcher"):
        print dispatcher_info
        if u"Qube6" in dispatcher_info.keys():
            dispatcherList.append(dispatcher.qube.Qube6(configInfo.getvalueJsonPath("[*].*.dispatcher.Qube6")[0]).getparam())
    print dispatcherList

    jobList = job.jobinfo.JobInfoList()
    if addFilePath is not None:
        jobList.get_joblist().append(job.jobinfo.JobInfo(fileParam,dispatcherList,configInfo))
    else:
        jobList.get_joblist().append(job.jobinfo.JobInfo(None, dispatcherList, configInfo.getvalueJsonPath("[*]")))

    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow(jobList,dispatcherList,configInfo.getvalueJsonPath("[*]"))
    main_window.show()


    sys.exit(app.exec_())
#    dispatcher.submit(job)
