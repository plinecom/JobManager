import abstract
import subprocess
import xml.etree.ElementTree


class Qube(abstract.DispatcherBase):
    def __init__(self):
       abstract.DispatcherBase.__init__(self)


class Qube6(Qube):
    def __init__(self, configdict):
        Qube.__init__(self)
        print configdict
        self._configdict = configdict
        self.setvalue("executable", self._configdict["submitter"])
        self.setvalue("server", "172.29.115.99")

        self.setvalue("dispatch_software", "Qube6")
        cmd = self._configdict["qbhosts"]+" --xml"

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout_data, stderr_data = p.communicate()

        qb_xml_document = xml.etree.ElementTree.fromstring("<doc>"+stdout_data+"</doc>")

        # print stdout_data

        group_dic = {}
        for e in qb_xml_document.findall("object/item/object/groups"):
            if e.text is not None:
                group_dic[e.text.encode("utf-8")] = "1"

        self.setvalue("groups", sorted(group_dic.keys()))
        # print group_dic.keys()

        cluster_dic = {}
        for e in qb_xml_document.findall("object/item/object/cluster"):
            cluster_dic[e.text.encode("utf-8")] = "1"
        cluster_dic2 = {}
        for cluster in cluster_dic.keys():
            cluster_level = cluster.split("/")
            for i in range(0,len(cluster_level)+1):
                cluster_dic2["/".join(cluster_level[0:i])] = 1
        # print cluster_dic2

        #    group_dic[e.text]="1"
        self.setvalue("pools", sorted(cluster_dic2.keys()))
        # print cluster_dic.keys()

#        self.setvalue("dispatherObj", self)

    def addJob(self,job):
        self._job.append(job)

    def submmision(self):
        self._buildCmd()

    def getDispatcherName(self):
        return "Qube 6"

    def submit(self,jobObj):
        print jobObj.getparam()
#        job = jobObj.getparam();
        cmd = self.getvalue("executable") + ' --name ' + jobObj.getvalue("jobName")\
            + ' --priority '+jobObj.getvalue("priority") \
            + ' --range '+jobObj.getvalue("startFrame") + '-' + jobObj.getvalue("endFrame")\
            + ' --chunk 10'
        if isinstance(jobObj.getvalue("selected_groups"), list):
            if len(jobObj.getvalue("selected_groups"))>0:
                cmd += ' --groups '+','.join(jobObj.getvalue("selected_groups"))
        cmd += ' /usr/autodesk/maya2014-x64/bin/Render -s QB_FRAME_START -e QB_FRAME_END ' \
            + jobObj.getvalue("filePath")
        # --groups string
        # --cluster string
        # --processors int
        # --supervisor
        # --range 1-100 --chunk 10
        print cmd

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout_data, stderr_data = p.communicate()

        print stdout_data
        print stderr_data

    def _buildCmd(self):
        for job in self._job:
            # if job.__class__.__name__ == "JobMayaSw":
                cmd = self.getvalue("executable") + ' -s ' + self.getvalue("server") + ' -u admin -b -department ' + getpass.getuser() + ' -e 566 -n ' + job.getvalue("job") + ' -f ' + job.getvalue("filePath") + ' -proj ' + job.getvalue("proj") + ' -sf ' + job.getvalue("startFrame") + " -ef " + job.getvalue("endFrame") + " -bf " + job.getvalue("byFrameSteps") + "  -se 0 -st 1 -attr MAYADIGITS 10 1 -max 1"
                print cmd
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                (stdout_data, stderr_data) = p.communicate()
                print stdout_data
                print stderr_data
