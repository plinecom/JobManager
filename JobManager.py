
import filelib.parser.lib
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
    def __init__(self,jobList, parent=None):
        PyQt4.QtGui.QMainWindow.__init__(self,parent)
        self._joblist = jobList
        print self._joblist.get_joblist()

        self.setAcceptDrops(True)

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
                            [file_parser.getparam()],
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

def loadFile(absPath):
    return job


if __name__ == "__main__":


    #addFilePath = "/root/test_maya_2015.mb"
    addFilePath = None

    if(len(sys.argv) > 1):
        addFilePath = sys.argv[1]

    script_dir_path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(script_dir_path,"config","config.json")
    print config_path
    config_file = open(config_path,'r')
    config = json.load(config_file)
    print config

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
    dispatcherList.append(dispatcher.qube.Qube6_6().getparam())
    print dispatcherList[0]

    jobList = job.jobinfo.JobInfoList()
    jobList.get_joblist().append(job.jobinfo.JobInfo([fileParam],dispatcherList,[config]))


    app = PyQt4.QtGui.QApplication(sys.argv)
    main_window = MainWindow(jobList)
    panel = PyQt4.QtGui.QWidget()
    panel.setObjectName("commonPanel")

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
