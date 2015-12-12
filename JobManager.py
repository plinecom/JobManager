
import filelib.parser.ma
import filelib.parser.mb
import os.path
import sys
import jobfactory.factory
import dispatcher.qube

import PyQt4.QtGui
import PyQt4.QtCore


if __name__ == "__main__":


    addFilePath = "/root/test_maya_2015.mb"

    if(len(sys.argv) > 1):
        addFilePath = sys.argv[1]


    #command line mode?

    (dir,jobExt) = os.path.splitext(addFilePath)
    jobExt = jobExt.lower()
    if jobExt == ".ma":
        fileParser = filelib.parser.ma.FileParserMayaMA(addFilePath)
    elif jobExt == ".mb":
        fileParser = filelib.parser.mb.FileParserMayaMB(addFilePath)
    fileParser.parse()
    print fileParser.getparam()
    job_factory = jobfactory.factory.JobFactory()
    job = job_factory.getJob(fileParser.getparam(), "SudioPlugin()")
    dispatcher = dispatcher.qube.Qube6_6()
    print dispatcher.getparam();


    app = PyQt4.QtGui.QApplication(sys.argv)
    main_window = PyQt4.QtGui.QMainWindow()
    main_window.setWindowTitle("JobManager")
    #main_window.setCentralWidget(panel)
    main_window.show()


    sys.exit(app.exec_())
#    dispatcher.submit(job)
