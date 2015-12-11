
import filelib.parser.ma
import filelib.parser.mb
import os.path
import sys

if __name__ == "__main__":
    addFilePath = "/root/test_maya_2015.mb"

    if(len(sys.argv) > 1):
        addFilePath = sys.argv[1]


    (dir,jobExt) = os.path.splitext(addFilePath)
    jobExt = jobExt.lower()
    if jobExt == ".ma":
        fileParser = filelib.parser.ma.FileParserMayaMA(addFilePath, SudioPlugin())
    elif jobExt == ".mb":
        fileParser = filelib.parser.mb.FileParserMayaMB(addFilePath)
    fileParser.parse()
    print fileParser.getparam()
#    job2 = fileParser.getJob()
    #jobfactory = JobFactory();
    #job2 = jobfactory.getJob(fileParser.getparam(), SudioPlugin())
