
import filelib.parser.ma
import filelib.parser.mb
import os.path
import sys
import jobfactory.factory
import dispatcher.qube

if __name__ == "__main__":


    addFilePath = "/root/test_maya_2015.mb"

    if(len(sys.argv) > 1):
        addFilePath = sys.argv[1]


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

    dispatcher.submit(job)
