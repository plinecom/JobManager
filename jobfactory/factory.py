from job import maya


class JobFactory():

#    def __init__(self):
#        pass

    def getJob(self, param, studio_plugin):

        job = None
#        param["chunksize"] = studio_plugin.getDefaultChunksize()
#        param["machineLimit"]= studio_plugin.getDefaultMachineLimit()

        if param["software"] == "Maya":
            job = maya.JobMaya(param)
        return job