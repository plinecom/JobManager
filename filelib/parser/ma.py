import abstract


__author__ = 'Masataka'


class FileParserMaya(abstract.FileParserBase):
    def __init__(self, filepath):
        abstract.FileParserBase.__init__(self, filepath)
        self._param["software"] = "Maya"


class FileParserMayaMA(FileParserMaya):
    def __init__(self, filepath):
        FileParserMaya.__init__(self, filepath)

    def parse_process(self):
        print "test3"

        f = file(self.getFilePath(),'r')

        version = None
        renderer = None

        frameStart = None
        frameEnd = None
        byFrameSteps = None

        outputFileExt = None
        outputFileExtVray = None
        outputPathFormat = None
        outputPathFormatVray = None

        renderLayerList=[]
        renderlayerEnable={}
        cameraList=['default']


        for l in f:
            #print l
            if version is None and 'fileInfo "product"' in l:
                temp = l
                version = temp.replace('fileInfo "product"','').lstrip().replace('"','').replace(";","").split()[1]
                print version
            if frameStart is None and ('setAttr ".fs"' in l or 'setAttr -k on ".fs"' in l):
                frameStart = l.split(' ')[-1].replace(';', '').replace('\n', '')
                if not frameStart.isdigit():
                    frameStart = "1"
            if frameEnd is None and ( 'setAttr ".ef"' in l or 'setAttr -k on ".ef"' in l):
                frameEnd = l.split(' ')[-1].replace(';', '').replace('\n', '')
            if byFrameSteps is None and 'setAttr -av ".bfs"' in l:
                byFrameSteps = l.split(' ')[-1].replace(';', '').replace('\n', '')
                if byFrameSteps == '".bfs"':
                    byFrameSteps = "1"

            if 'createNode camera ' in l:
                camera = l.split(' ')[-1].replace('"','').replace(';','').rstrip()
                cameraList.append(camera)
            if 'createNode renderLayer -n' in l:
                renderLayer = l.split(' ')[-1].replace('"','').replace(';','').rstrip()
                renderLayerList.append(renderLayer)
                renderlayerEnable[renderLayer] = True
                for i in range(0,2):
                    line = f.next()
                    if 'setAttr ".rndr" no;' in line:
                        renderlayerEnable[renderLayer]= False
                        break


            if outputFileExt is None and ('setAttr ".imfkey" -type' in l or 'setAttr -cb on ".imfkey" -type' in l):
                outputFileExt = "."+l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"','')
            if outputPathFormat is None and ( 'setAttr ".ifp" -type' in l or 'setAttr -cb on ".ifp" -type' in l):
                outputPathFormat = l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"','')
            if outputFileExtVray is None and ( 'setAttr ".imgfs" -type' in l or 'setAttr -cb on ".imgfs" -type' in l):
                outputFileExtVray = "."+l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"','')
            if outputPathFormatVray is None and ('setAttr ".fnprx" -type' in l or 'setAttr -cb on ".fnprx" -type' in l):
                outputPathFormatVray = l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"','')

            if renderer is None and ('setAttr ".ren" -type' in l or 'setAttr -cb on ".ren" -type' in l):
                print l;
                temp = l.split(' ')[-1]
                if 'mentalRay' in temp:
                    renderer = 'mentalray'
                elif 'vray' in temp:
                    renderer = 'vray'
                elif 'arnold' in temp:
                    renderer = 'arnold'
                elif 'mayaHardware' in temp:
                    renderer = 'maya_hardware'
                else:
                    renderer = 'maya_file'

                print renderer
                break;
        if renderer is None:
            renderer = 'file'
        print renderer
        print renderlayerEnable
        if frameStart is None:
            frameStart = "1"
        if frameEnd is None:
            frameEnd = str(int(frameStart)+9)
        if byFrameSteps is None:
            byFrameSteps = "0"

        self._param["filePath"]= self.getFilePath()
        self._param["version"]=version
        self._param["application"]="Maya_"+version
        self._param["renderer"]=renderer

        self._param["startFrame"]=frameStart
        self._param["endFrame"]=frameEnd
        self._param["byFrameSteps"]=byFrameSteps

        self._param["outputFileExt"]=outputFileExt
        self._param["outputFileExtVray"]=outputFileExtVray
        self._param["outputPathFormat"]=outputPathFormat
        self._param["opuputPathFormatVray"]=outputPathFormatVray

        self._param["renderLayerList"]=renderLayerList
        self._param["renderLayerEnable"]=renderlayerEnable
        self._param["cameraList"]=cameraList

        print self._param

        f.close()
