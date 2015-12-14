import jobinfo

__author__ = 'Masataka'


class JobMaya(jobinfo.JobInfo):
    def __init__(self,param):
        jobinfo.JobInfo.__init__(self, param)


class JobMayaSw(JobMaya):
    def __init__(self,param):
        JobMaya.__init__(self,param)


class JobMayaMr(JobMaya):
    def __init__(self,param):
        JobMaya.__init__(self,param)


class JobMayaFile(JobMaya):
    def __init__(self,param):
        JobMaya.__init__(self,param)
