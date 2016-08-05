import ma
import mb
import os.path


def file_parse(abs_path):
    (directory, job_ext) = os.path.splitext(abs_path)
    job_ext = job_ext.lower()
    if job_ext == ".ma":
        file_parser = ma.FileParserMayaMA(abs_path)
    elif job_ext == ".mb":
        file_parser = mb.FileParserMayaMB(abs_path)

    file_parser.parse()

    return file_parser
