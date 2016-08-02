__author__ = 'Masataka'
import struct
import binascii
import filelib.parser.ma


class FileParserMayaMB(filelib.parser.ma.FileParserMaya):
    def __init__(self, filepath):
       filelib.parser.ma.FileParserMaya.__init__(self, filepath)

    def parse_process(self):

        version = None
        renderer = None

        frameStart = None
        frameEnd = None
        byFrameSteps = None
        fpsData = None
        typeInfo = None

        outputFileExt = None
        outputFileExtVray = None
        outputPathFormat = None
        outputPathFormatVray = None

        renderLayerList = []
        renderlayerEnable = {}
        cameraList = ['default']

#        for renderLayer in job["renderLayerList"]:
#            res["renderLayerEnable"][renderLayer]= True

        f = file(self.getFilePath(), 'rb')
        for l in f:
            if version is None and 'version' in l:
                version = l.split('version')[1][1:5]
            if frameStart is None and ('fs\0 ' in l):
                # print "sisi"
                print l.split('fs\0 ')[0]
                print binascii.hexlify(l.split('fs\0 ')[0][-1])
#                frameStart = struct.unpack('>i',l.split('fs\0 ')[0][1:5])[0]
#                frameStart = l.split('fs')[1][1:5]
                frameStart = struct.unpack('>i', l.split('fs\0 ')[0][-4:])[0]
                print str(frameStart)
            if frameEnd is None and ('ef\0 ' in l):
                print binascii.hexlify(l.split('ef\0 ')[0][-1])
                frameEnd = struct.unpack('>i', l.split('ef\0 ')[0][-4:])[0]
                print str(frameEnd)
            if byFrameSteps is None and ('bfs ' in l):
                print binascii.hexlify(l.split('bfs ')[0][-1])
                byFrameSteps = struct.unpack('>i', l.split('bfs ')[0][-4:])[0]
                print str(byFrameSteps)
            if fpsData is None and 'TUNI' in l:

                type = l.split('TUNI')[1][1:100]
                fpsData = 0
                print "test-"
                print type
                if 'ntscf' in type:
                    fpsData = 60
                    typeInfo = 'ntscf'
                elif 'ntsc' in type:
                    fpsData = 30
                    typeInfo = 'ntsc'
                elif 'palf' in type:
                    fpsData = 50
                    typeInfo = 'palf'
                elif 'pal' in type:
                    fpsData = 25
                    typeInfo = 'pal'
                elif 'film' in type:
                    fpsData = 24
                    typeInfo = 'film'
                elif 'game' in type:
                    fpsData = 15
                    typeInfo = 'game'
                elif 'show' in type:
                    fpsData = 48
                    typeInfo = 'show'
                else:
                    print "else"
                    fpsData = 60
            if renderer is None and 'ren\0' in l:
                ren = l.split('ren\0')[1][1:100]
                if 'mentalRay' in ren:
                    renderer = 'mentalray'
                elif 'mayaHardware' in ren:
                    renderer = 'maya_hardware'
                elif 'vray' in ren:
                    renderer = 'vray'
                elif 'arnold' in ren:
                    renderer = 'arnold'
                else:
                    print "ren"
                    print ren
                    renderer = 'maya_software'
            if "RNDLCREA" in l:
                renderLayerInfoList = l.split("RNDLCREA")
                for renderLayerInfo in renderLayerInfoList:
                    layerInfo = renderLayerInfo[0:50]
                    layerNameInfoList = layerInfo.split('\0')
                    for layerNameInfo in layerNameInfoList:
                        if layerNameInfo != '':
                            if layerNameInfo == 'masterLayer':
                                layerNameInfo = 'defaultRenderLayer'
                            if len(layerNameInfo) > 1 and layerNameInfo.isalnum() and 'DBLE' not in layerNameInfo and 'FLGS' not in layerNameInfo and 'rlmi' not in layerNameInfo and 'rndr' not in layerNameInfo:
                                renderLayerList.append(layerNameInfo)
#                for renderLayerInfo in renderLayerInfoList:
#                    layerInfo = renderLayerInfo[0:100];
#                    if 'rndr' in layerInfo:
#                       for renderLayer in renderLayerList:
#                           if renderLayer == '':
#                               continue
#                           rendLayer = renderLayer
#                           if renderLayer == 'masterLayer':
#                               rendLayer = 'defaultRenderLayer'
#                           if rendLayer in layerInfo:
#                               renderLayerEnable[renderLayer] = False
            if "DCAMCREA" in l:
                cameraInfoList = l.split("DCAMCREA")
                for cameraInfo in cameraInfoList:
                    camInfo = cameraInfo[0:50]
                    cameraNameInfoList = camInfo.split('\0')
                    size = len(cameraNameInfoList)
                    i = 0
                    for cameraNameInfo in cameraNameInfoList:
                        if cameraNameInfo != '':
                            if i >= 1:
                                if len(cameraNameInfo) > 1 and 'DBL3' not in cameraNameInfo and 'XFRMCREA' not in cameraNameInfo:
                                    cameraList.append(cameraNameInfo)
#                                   print cameraNameInfo
                                break
                            i+=1
        if frameStart is None:
            self._param["startFrame"] = "1"
        else:
            # print "tx"
            # print frameStart
            # print fpsData
            self._param["startFrame"]=str(frameStart*fpsData/100.0/60.0)
        if frameEnd is None:
            self._param["endFrame"] = "10"
        else:
            self._param["endFrame"]=str(frameEnd*fpsData/100.0/60.0)
        if byFrameSteps is None:
            byFrameSteps = "1"
        if renderer is None:
            renderer = 'sw'

        self._param["version"] = version
        self._param["application"] = "Maya_"+version
        self._param["renderer"] = renderer
        self._param["type"] = typeInfo

        self._param["byFrameSteps"] = str(byFrameSteps)

        self._param["outputFileExt"] = outputFileExt
        self._param["outputFileExtVray"] = outputFileExtVray
        self._param["outputPathFormat"] = outputPathFormat
        self._param["opuputPathFormatVray"] = outputPathFormatVray

        self._param["renderLayerList"] = renderLayerList
        self._param["renderLayerEnable"] = renderlayerEnable
        self._param["cameraList"] = cameraList

        print self._param

        return ""
