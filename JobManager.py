
import filelib.parser.ma
import filelib.parser.mb
import os.path
import sys
import jobfactory.factory
import dispatcher.qube

import PyQt4.QtGui
import PyQt4.QtCore

import json
import job.jobinfo

import gui.submit.common

class MainWindow(PyQt4.QtGui.QMainWindow):
    def __init__(self, parent=None):
        PyQt4.QtGui.QMainWindow.__init__(self,parent)

        self.setAcceptDrops(True)
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for u in event.mimeData().urls():
            print u.toLocalFile()

if __name__ == "__main__":


    addFilePath = "/root/test_maya_2015.mb"

    if(len(sys.argv) > 1):
        addFilePath = sys.argv[1]

    script_dir_path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(script_dir_path,"config","config.json")
    print config_path
    config_file = open(config_path,'r')
    config = json.load(config_file)
    print config

    #command line mode?

    (dir,jobExt) = os.path.splitext(addFilePath)
    jobExt = jobExt.lower()
    if jobExt == ".ma":
        fileParser = filelib.parser.ma.FileParserMayaMA(addFilePath)
    elif jobExt == ".mb":
        fileParser = filelib.parser.mb.FileParserMayaMB(addFilePath)
    fileParser.parse()
    print fileParser.getparam()
#    job_factory = jobfactory.factory.JobFactory()
#    job = job_factory.getJob(fileParser.getparam(), "SudioPlugin()")
    dispatcherList = []
    dispatcherList.append(dispatcher.qube.Qube6_6())
    print dispatcherList[0].getparam()

    jobList = []
    jobList.append(job.jobinfo.JobInfo(fileParser.getparam(),dispatcherList,config))


    app = PyQt4.QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    panel = PyQt4.QtGui.QWidget()

    #main_window.setAcceptDrops(True)

    common_panel = gui.submit.common.CommonPanel(jobList, panel)
    pannel_layout = PyQt4.QtGui.QVBoxLayout()
    pannel_layout.addWidget(common_panel)
    panel.setLayout(pannel_layout)


    main_window.setWindowTitle("JobManager")
    main_window.setCentralWidget(panel)
    main_window.show()


    sys.exit(app.exec_())
#    dispatcher.submit(job)
