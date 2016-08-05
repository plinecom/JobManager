import struct
import binascii
import filelib.parser.ma

__author__ = 'Masataka'


class FileParserMayaMB(filelib.parser.ma.FileParserMaya):
    def __init__(self, file_path):
        filelib.parser.ma.FileParserMaya.__init__(self, file_path)

    @property
    def parse_process(self):

        version = None
        renderer = None

        frame_start = None
        frame_end = None
        by_frame_steps = None
        fps_data = None
        type_info = None

        output_file_ext = None
        output_file_ext_vray = None
        output_path_format = None
        output_path_format_vray = None

        render_layer_list = []
        render_layer_enable = {}
        camera_list = ['default']

#        for renderLayer in job["render_layer_list"]:
#            res["renderLayerEnable"][renderLayer]= True

        f = file(self.get_file_path(), 'rb')
        for l in f:
            if version is None and 'version' in l:
                version = l.split('version')[1][1:5]
            if frame_start is None and ('fs\0 ' in l):
                # print "sisi"
                print l.split('fs\0 ')[0]
                print binascii.hexlify(l.split('fs\0 ')[0][-1])
#                frame_start = struct.unpack('>i',l.split('fs\0 ')[0][1:5])[0]
#                frame_start = l.split('fs')[1][1:5]
                frame_start = struct.unpack('>i', l.split('fs\0 ')[0][-4:])[0]
                print str(frame_start)
            if frame_end is None and ('ef\0 ' in l):
                print binascii.hexlify(l.split('ef\0 ')[0][-1])
                frame_end = struct.unpack('>i', l.split('ef\0 ')[0][-4:])[0]
                print str(frame_end)
            if by_frame_steps is None and ('bfs ' in l):
                print binascii.hexlify(l.split('bfs ')[0][-1])
                by_frame_steps = struct.unpack('>i', l.split('bfs ')[0][-4:])[0]
                print str(by_frame_steps)
            if fps_data is None and 'TUNI' in l:

                movie_type = l.split('TUNI')[1][1:100]

                print "test-"
                print movie_type
                if 'ntscf' in movie_type:
                    fps_data = 60
                    type_info = 'ntscf'
                elif 'ntsc' in movie_type:
                    fps_data = 30
                    type_info = 'ntsc'
                elif 'palf' in movie_type:
                    fps_data = 50
                    type_info = 'palf'
                elif 'pal' in movie_type:
                    fps_data = 25
                    type_info = 'pal'
                elif 'film' in movie_type:
                    fps_data = 24
                    type_info = 'film'
                elif 'game' in movie_type:
                    fps_data = 15
                    type_info = 'game'
                elif 'show' in movie_type:
                    fps_data = 48
                    type_info = 'show'
                else:
                    print "else"
                    fps_data = 60
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
                render_layer_info_list = l.split("RNDLCREA")
                for renderLayerInfo in render_layer_info_list:
                    layer_info = renderLayerInfo[0:50]
                    layer_name_info_list = layer_info.split('\0')
                    for layer_name_info in layer_name_info_list:
                        if layer_name_info != '':
                            if layer_name_info == 'masterLayer':
                                layer_name_info = 'defaultRenderLayer'
                            if len(layer_name_info) > 1 and layer_name_info.isalnum() and 'DBLE' not in layer_name_info:
                                if 'FLGS' not in layer_name_info:
                                    if 'rlmi' not in layer_name_info:
                                        if 'rndr' not in layer_name_info:
                                            render_layer_list.append(layer_name_info)
            #                for renderLayerInfo in render_layer_info_list:
            #                    layer_info = renderLayerInfo[0:100];
            #                    if 'rndr' in layer_info:
            #                       for renderLayer in render_layer_list:
            #                           if renderLayer == '':
            #                               continue
            #                           rendLayer = renderLayer
            #                           if renderLayer == 'masterLayer':
            #                               rendLayer = 'defaultRenderLayer'
            #                           if rendLayer in layer_info:
            #                               renderLayerEnable[renderLayer] = False
            if "DCAMCREA" in l:
                camera_info_list = l.split("DCAMCREA")
                for camera_info in camera_info_list:
                    cam_info = camera_info[0:50]
                    camera_name_info_list = cam_info.split('\0')

                    i = 0
                    for camera_name_info in camera_name_info_list:
                        if camera_name_info != '':
                            if i >= 1:
                                if len(camera_name_info) > 1 and 'DBL3' not in camera_name_info:
                                    if 'XFRMCREA' not in camera_name_info:
                                        camera_list.append(camera_name_info)
    #                                   print camera_name_info
                                break
                            i += 1
        if frame_start is None:
            self._param["startFrame"] = "1"
        else:
            # print "tx"
            # print frame_start
            # print fps_data
            self._param["startFrame"] = str(frame_start*fps_data/100.0/60.0)
        if frame_end is None:
            self._param["endFrame"] = "10"
        else:
            self._param["endFrame"] = str(frame_end*fps_data/100.0/60.0)
        if by_frame_steps is None:
            by_frame_steps = "1"
        if renderer is None:
            renderer = 'sw'

        self._param["version"] = version
        self._param["application"] = "Maya_"+version
        self._param["renderer"] = renderer
        self._param["movie_type"] = type_info

        self._param["by_frame_steps"] = str(by_frame_steps)

        self._param["output_file_ext"] = output_file_ext
        self._param["output_file_ext_vray"] = output_file_ext_vray
        self._param["output_path_format"] = output_path_format
        self._param["opuputPathFormatVray"] = output_path_format_vray

        self._param["render_layer_list"] = render_layer_list
        self._param["renderLayerEnable"] = render_layer_enable
        self._param["camera_list"] = camera_list

        print self._param

        return ""
