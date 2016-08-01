import ma
import mb
import os.path


def fileParse(abs_path):
    (directory, jobExt) = os.path.splitext(abs_path)
    jobExt = jobExt.lower()
    if jobExt == ".ma":
        fileParser = ma.FileParserMayaMA(abs_path)
    elif jobExt == ".mb":
        fileParser = mb.FileParserMayaMB(abs_path)

    fileParser.parse()

    return fileParser