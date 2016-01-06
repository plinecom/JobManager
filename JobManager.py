
import filelib.parser.lib
import os.path
import sys
import jobfactory.factory
import dispatcher.qube

from PyQt4 import QtGui, QtCore

import yaml
import job.jobinfo
import config.auto.autoconf
import config.config
import gui.submit.common
import gui.submit.maya

class MainWindow(QtGui.QMainWindow):
    def __init__(self,jobList, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self._joblist = jobList
        print self._joblist.get_joblist()

        self.setAcceptDrops(True)
        panel = QtGui.QWidget()
        panel.setObjectName("commonPanel")

        #main_window.setAcceptDrops(True)

        common_panel = gui.submit.common.CommonPanel(jobList, panel)
        maya_panel = gui.submit.maya.MayaPanel(jobList, panel)
        qtab = QtGui.QTabWidget()
        qtab.addTab(common_panel, "common")
        qtab.addTab(maya_panel, "Maya")


        panel_layout = QtGui.QVBoxLayout()
        panel_layout.addWidget(qtab)

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
        qtabL.addTab(QtGui.QListWidget(self),"Job")



        txtBrowser = QtGui.QTextBrowser()
        txtBrowser.append("test")
        qsplitV.addWidget(qtabL)
        qsplitV.addWidget(txtBrowser)

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
            self._joblist.get_joblist().append(
                    job.jobinfo.JobInfo(
                            file_parser.getparam(),
                            self._joblist.get_current_job().getlist_dispatcher(),
                            self._joblist.get_current_job().getparam_config()
                    )
            )

            print self._joblist.get_current_job()

        self._joblist.set_current_job_id(-1)
#        common_panel = self.findChild(gui.submit.common.CommonPanel, "commonPanel")
        common_panel = self.findChild(gui.submit.common.CommonPanel)
        print common_panel
        common_panel.update_ui()
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
    configInfo = config.config.ConfigInfo(configList)
#    print configInfo.getvalue("priority")
#    print configInfo.getvalue("priority")
    configInfo.getvalueJsonPath("[*].*.priority")
    configInfo.getvalueJsonPath("[*].*.dispatcher")
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
    for dispatcher_name in configInfo.getvalue("dispatcher").keys():
        if dispatcher_name == "Qube6":
          dispatcherList.append(dispatcher.qube.Qube6(configInfo.getvalue("dispatcher")[dispatcher_name]).getparam())
    print dispatcherList

    jobList = job.jobinfo.JobInfoList()
    jobList.get_joblist().append(job.jobinfo.JobInfo(fileParam,dispatcherList,configInfo))


    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow(jobList)
    main_window.show()


    sys.exit(app.exec_())
#    dispatcher.submit(job)
