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

        outputFileExt = None
        outputFileExtVray = None
        outputPathFormat = None
        outputPathFormatVray = None

        renderLayerList=[]
        renderlayerEnable={}
        cameraList=['default']

#        for renderLayer in job["renderLayerList"]:
#            res["renderLayerEnable"][renderLayer]= True

        f = file(self.getFilePath(), 'rb')
        for l in f:
            if version is None and 'version' in l:
                version = l.split('version')[1][1:5]
            if frameStart is None and ('fs\0 ' in l):
                print "sisi"
                print l.split('fs\0 ')[0]
                print binascii.hexlify(l.split('fs\0 ')[0][-1])
#                frameStart = struct.unpack('>i',l.split('fs\0 ')[0][1:5])[0]
#                frameStart = l.split('fs')[1][1:5]
                frameStart = struct.unpack('>i',l.split('fs\0 ')[0][-4:])[0]
                print str(frameStart)
            if frameEnd is None and ( 'ef\0 ' in l):
                print binascii.hexlify(l.split('ef\0 ')[0][-1])
                frameEnd = struct.unpack('>i',l.split('ef\0 ')[0][-4:])[0]
                print str(frameEnd)
            if byFrameSteps is None and ( 'bfs ' in l):
                print binascii.hexlify(l.split('bfs ')[0][-1])
                byFrameSteps = struct.unpack('>i',l.split('bfs ')[0][-4:])[0]
                print str(byFrameSteps)
            if fpsData is None and 'TUNI' in l:

                type = l.split('TUNI')[1][1:100]
                fpsData = 0
                if 'ntscf' in type:
                    fpsData = 60
                elif 'ntsc' in type:
                    fpsData = 30
                elif 'palf' in type:
                    fpsData = 50
                elif 'palf' in type:
                    fpsData = 50
                elif 'pal' in type:
                    fpsData = 25
                elif 'film' in type:
                    fpsData = 24
                elif 'game' in type:
                    fpsData = 15
                elif 'show' in type:
                    fpsData = 48
                else:
                    fpsData = 60
            if renderer is None and 'ren\0' in l:
                ren = l.split('ren\0')[1][1:100]
                if 'mentalRay' in ren:
                    renderer = 'mr'
                elif 'mayaHardware' in ren:
                    renderer = 'hw'
                elif 'vray' in ren:
                    renderer = 'vray'
                else:
                    renderer = 'sw'
            if "RNDLCREA" in l:
                renderLayerInfoList = l.split("RNDLCREA");
                for renderLayerInfo in renderLayerInfoList:
                    layerInfo = renderLayerInfo[0:50];
                    layerNameInfoList = layerInfo.split('\0')
                    for layerNameInfo in layerNameInfoList:
                        if layerNameInfo !='':
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
                cameraInfoList = l.split("DCAMCREA");
                for cameraInfo in cameraInfoList:
                    camInfo = cameraInfo[0:50]
                    cameraNameInfoList = camInfo.split('\0');
                    size = len(cameraNameInfoList);
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
            self._param["startFrame"]=str(frameStart*fpsData/100.0/60.0)
        if frameEnd is None:
            self._param["endFrame"] = "10"
        else:
            self._param["endFrame"]=str(frameEnd*fpsData/100.0/60.0)
        if byFrameSteps is None:
            byFrameSteps = "1"
        if renderer is None:
            renderer = 'sw'

        self._param["version"]=version
        self._param["application"]="Maya "+version
        self._param["renderer"]=renderer

        self._param["byFrameSteps"]=str(byFrameSteps)

        self._param["outputFileExt"]=outputFileExt
        self._param["outputFileExtVray"]=outputFileExtVray
        self._param["outputPathFormat"]=outputPathFormat
        self._param["opuputPathFormatVray"]=outputPathFormatVray

        self._param["renderLayerList"]=renderLayerList
        self._param["renderLayerEnable"]=renderlayerEnable
        self._param["cameraList"]=cameraList

        print self._param

        return ""

        for line in f:
            if "RNDLCREA" in line:
                renderLayerInfoList = line.split("RNDLCREA");
                for renderLayerInfo in renderLayerInfoList:
                    layerInfo = renderLayerInfo[0:100];
                    if 'rndr' in layerInfo:
                       for renderLayer in job["renderLayerList"]:
                           if renderLayer == '':
                               continue
                           rendLayer = renderLayer
                           if renderLayer == 'masterLayer':
                               rendLayer = 'defaultRenderLayer'
                           if rendLayer in layerInfo:
                               res["renderLayerEnable"][renderLayer] = False
            elif "DCAMCREA" in line:
                cameraInfoList = line.split("DCAMCREA");
                for cameraInfo in cameraInfoList:
                    camInfo = cameraInfo[0:50]
                    cameraNameInfoList = camInfo.split('\0');
                    size = len(cameraNameInfoList);
                    i = 0
                    for cameraNameInfo in cameraNameInfoList:
                        if cameraNameInfo != '':
                            if i >= 1:
                                if len(cameraNameInfo) > 1 and 'DBL3' not in cameraNameInfo and 'XFRMCREA' not in cameraNameInfo:
                                    res["cameraList"].append(cameraNameInfo)
#                                    print cameraNameInfo
                                break
                            i+=1
        fps = 24
        while True:
            buf = mb.read(4)
            if buf == 'vers':
                ver = mb.read(32)
                res['application'] = checkVersion(ver)
                res['versionIndex'] = checkVersionIndex(ver)
                break
            if buf == 'TUNI':
                fpsData = mb.read(8)
                if 'ntscf' in fpsData:
                    fps = 60
                elif 'ntsc' in fpsData:
                    fps = 30
                elif 'palf' in fpsData:
                    fps = 50
                elif 'palf' in fpsData:
                    fps = 50
                elif 'pal' in fpsData:
                    fps = 25
                elif 'film' in fpsData:
                    fps = 24
                elif 'game' in fpsData:
                    fps = 15
                elif 'show' in fpsData:
                    fps = 48
            if buf == 'XFRM':
                break

        renderUnLoaded = True
        frameStartUnLoaded = True
        frameEndUnLoaded = True
#    print 'seekend'
#    print 'seekendend'
        bufferLength = 4096
        buffer =''
        id = 0
        bufold=''
        while (renderUnLoaded or frameStartUnLoaded or frameEndUnLoaded) and pos >= 0:
            pos -= bufferLength
            mb.seek(pos)
            buffer = mb.read(bufferLength)
            id = 0;
            while (renderUnLoaded or frameStartUnLoaded or frameEndUnLoaded) and id <bufferLength:

                id += 4
                buf = buffer[bufferLength-id:bufferLength-id+4]
                hexlify_buf = binascii.hexlify(buf)
                if '7d' in hexlify_buf: # }
                    if '7d0a' in hexlify_buf + binascii.hexlify(bufold):
                        pass
                    renderUnLoaded = False
                    frameStartUnLoaded = False
                    frameEndUnLoaded = False
                elif hexlify_buf == '00280000': # / (
                 #print 'ma'
                 #print binascii.hexlify(buf)
                 #print "["+buf+"]"
                     renderUnLoaded = False
                     frameStartUnLoaded = False
                     frameEndUnLoaded = False
                elif hexlify_buf == '2f204d61': # / Ma
                     renderUnLoaded = False
                     frameStartUnLoaded = False
                     frameEndUnLoaded = False
                elif renderUnLoaded and hexlify_buf == '72656e00': #ren
                     readSize = min(id,512)
                     ren = buffer[bufferLength-id+4:bufferLength-id+4+readSize]
                     if 'mentalRay' in ren:
                         res["renderer"] = 'mr'
                     elif 'mayaHardware' in ren:
                         res["renderer"] = 'hw'
                     elif 'vray' in ren:
                         res["renderer"] = 'vray'
                     renderUnLoaded = False
                elif frameStartUnLoaded and hexlify_buf == '66730020': #fs
                     fs = bufold
                     fvalue = struct.unpack('>i',fs)[0]*fps/100.0/60.0
                     ivalue = int(fvalue)
                     if(ivalue == fvalue):
                         res["frameStart"] = str(ivalue)
                     else:
                         res["frameStart"] = str(fvalue)
                     frameStartUnLoaded = False
                #print 'fs'
                elif frameEndUnLoaded and hexlify_buf == '65660020': #ef62 66 73 00
                     ef = bufold
                     fvalue = struct.unpack('>i',ef)[0]*fps/100.0/60.0
                     ivalue = int(fvalue)
                     if(ivalue == fvalue):
                        res["frameEnd"] = str(ivalue)
                     else:
                        res["frameEnd"] = str(fvalue)
                     frameEndUnLoaded = False
                     #print 'ef'
                elif hexlify_buf == '62667300': #bfs
                    dble = binascii.hexlify(bufold)[4:]
                    exp = int(dble[0],16);
                    value = float(int(dble[1:],16))
                    if exp > 0:
                        bfs = value * pow(2,exp-1)/1024 + pow(2,exp+1)
                    else:
                        bfs = value/1024+1

                    fvalue = bfs
                    ivalue = int(fvalue)
                    if(ivalue == fvalue):
                        res["byFrameSteps"] = str(ivalue)
                    else:
                        res["byFrameSteps"] = str(fvalue)
                elif buf == 'imfk':
                    if 'imfkey' in buffer[bufferLength-id:bufferLength-id+8]:
                        res["outputFileExt"] = "."+buffer[bufferLength+8-id:bufferLength-id+8+4].replace('\0','')
                        print res["outputFileExt"]
                elif hexlify_buf == '69667000': # ifp
                    outputPathFormat =''
                    for i in range(1,100):
                        buf2 = buffer[bufferLength+(i*4)-id:bufferLength-id+(i*4)+4]
                        if binascii.hexlify(buf2) == '53545220': # STR
                            break;
                        outputPathFormat += buf2.replace('\0','')
                    res["outputPathFormat"] = outputPathFormat[1:]
                    print "["+res["outputPathFormat"]+"]"
                bufold = buf[:]
        f.close()
