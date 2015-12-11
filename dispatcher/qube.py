import abstract
import subprocess
import xml.etree.ElementTree
__author__ = 'Masataka'


class Qube(abstract.DispatcherBase):
    def __init__(self):
       abstract.DispatcherBase.__init__(self)


class Qube6_6(Qube):
    def __init__(self):
        Qube.__init__(self)
        self.setValue("executable","/usr/local/pfx/qube/bin/qbsub")
        self.setValue("server","172.29.115.99")

        cmd = "/usr/local/pfx/qube/bin/qbhosts --xml"

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout_data, stderr_data = p.communicate()

        qb_xml_document = xml.etree.ElementTree.fromstring("<doc>"+stdout_data+"</doc>")

        #print stdout_data

        group_dic = {}
        for e in qb_xml_document.findall("object/item/object/groups"):
            group_dic[e.text] = "1"

        self.setValue("groups",group_dic.keys())
        print group_dic.keys()

        cluster_dic = {}
        for e in qb_xml_document.findall("object/item/object/cluster"):
            cluster_dic[e.text] = "1"
        #    group_dic[e.text]="1"
        self.setValue("clusters",cluster_dic.keys())
        print cluster_dic.keys()

    def addJob(self,job):
        self._job.append(job)

    def submmision(self):
        self._buildCmd()

    def getDispatcherName(self):
        return "Qube 6.6"

    def submit(self,jobObj):
        job = jobObj.getparam();
        cmd = self.getValue("executable")+' --name myjobrx --prototype cmdrange --priority 9998 --range 1-200 --chunk 10 ls -s QB_FRAME_START -e QB_FRAME_END ' +job["fileInfo"]["filePath"]
        #--groups string
        #--cluster string
        #--processors int
        #--supervisor
        #--range 1-100 --chunk 10
        print cmd

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout_data, stderr_data = p.communicate()

        print stdout_data
        print stderr_data

    def _buildCmd(self):
        for job in self._job:
     #       if job.__class__.__name__ == "JobMayaSw":
                cmd = self.getValue("executable")+' -s '+self.getValue("server")+' -u admin -b -department '+getpass.getuser()+' -e 566 -n '+job.getValue("job")+' -f '+job.getValue("filePath")+' -proj '+job.getValue("proj")+' -sf '+job.getValue("startFrame") +" -ef "+job.getValue("endFrame") +" -bf "+job.getValue("byFrameSteps") +"  -se 0 -st 1 -attr MAYADIGITS 10 1 -max 1"
                print cmd
                p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
                ( stdoutdata,stderrdata )= p.communicate()
                print stdoutdata
                print stderrdata
