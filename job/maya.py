import abstract

__author__ = 'Masataka'


class JobMaya(abstract.JobBase):
    def __init__(self,param):
        abstract.JobBase.__init__(self,param)


class JobMayaSw(JobMaya):
    def __init__(self,param):
        JobMaya.__init__(self,param)


class JobMayaMr(JobMaya):
    def __init__(self,param):
        JobMaya.__init__(self,param)


class JobMayaFile(JobMaya):
    def __init__(self,param):
        JobMaya.__init__(self,param)
