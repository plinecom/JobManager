import abstract


__author__ = 'Masataka'


class FileParserMaya(abstract.FileParserBase):
    def __init__(self, file_path):
        abstract.FileParserBase.__init__(self, file_path)
        self._param["software"] = "Maya"


class FileParserMayaMA(FileParserMaya):
    def __init__(self, file_path):
        FileParserMaya.__init__(self, file_path)

    def parse_process(self):
        print "test3"

        f = file(self.get_file_path(), 'r')

        version = None
        renderer = None

        frame_start = None
        frame_end = None
        by_frame_steps = None

        output_file_ext = None
        output_file_ext_vray = None
        output_path_format = None
        output_path_format_vray = None

        render_layer_list = []
        renderlayer_enable = {}
        camera_list = ['default']

        for l in f:
            # print l
            if version is None and 'fileInfo "product"' in l:
                temp = l
                version = temp.replace('fileInfo "product"', '').lstrip().replace('"', '').replace(";", "").split()[1]
                print version
            if frame_start is None and ('setAttr ".fs"' in l or 'setAttr -k on ".fs"' in l):
                frame_start = l.split(' ')[-1].replace(';', '').replace('\n', '')
                if not frame_start.isdigit():
                    frame_start = "1"
            if frame_end is None and ('setAttr ".ef"' in l or 'setAttr -k on ".ef"' in l):
                frame_end = l.split(' ')[-1].replace(';', '').replace('\n', '')
            if by_frame_steps is None and 'setAttr -av ".bfs"' in l:
                by_frame_steps = l.split(' ')[-1].replace(';', '').replace('\n', '')
                if by_frame_steps == '".bfs"':
                    by_frame_steps = "1"

            if 'createNode camera ' in l:
                camera = l.split(' ')[-1].replace('"', '').replace(';', '').rstrip()
                camera_list.append(camera)
            if 'createNode render_layer -n' in l:
                render_layer = l.split(' ')[-1].replace('"', '').replace(';', '').rstrip()
                render_layer_list.append(render_layer)
                renderlayer_enable[render_layer] = True
                for i in range(0, 2):
                    line = f.next()
                    if 'setAttr ".rndr" no;' in line:
                        renderlayer_enable[render_layer] = False
                        break

            if output_file_ext is None and ('setAttr ".imfkey" -type' in l or 'setAttr -cb on ".imfkey" -type' in l):
                output_file_ext = "."+l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"', '')
            if output_path_format is None and ('setAttr ".ifp" -type' in l or 'setAttr -cb on ".ifp" -type' in l):
                output_path_format = l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"', '')
            if output_file_ext_vray is None and ('setAttr ".imgfs" -type' in l or 'setAttr -cb on ".imgfs" -type' in l):
                output_file_ext_vray = "."+l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"', '')
            if output_path_format_vray is None:
                if 'setAttr ".fnprx" -type' in l or 'setAttr -cb on ".fnprx" -type' in l:
                    output_path_format_vray = l.split(' ')[-1].replace(';', '').replace('\n', '').replace('"', '')

            if renderer is None and ('setAttr ".ren" -type' in l or 'setAttr -cb on ".ren" -type' in l):
                print l
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
                break

        if renderer is None:
            renderer = 'file'
        # print renderer
        # print renderlayer_enable
        if frame_start is None:
            frame_start = "1"
        if frame_end is None:
            frame_end = str(int(frame_start)+9)
        if by_frame_steps is None:
            by_frame_steps = "0"

        self._param["filePath"] = self.get_file_path()
        self._param["version"] = version
        self._param["application"] = "Maya_"+version
        self._param["renderer"] = renderer

        self._param["startFrame"] = frame_start
        self._param["endFrame"] = frame_end
        self._param["by_frame_steps"] = by_frame_steps

        self._param["output_file_ext"] = output_file_ext
        self._param["output_file_ext_vray"] = output_file_ext_vray
        self._param["output_path_format"] = output_path_format
        self._param["opuputPathFormatVray"] = output_path_format_vray

        self._param["render_layer_list"] = render_layer_list
        self._param["renderLayerEnable"] = renderlayer_enable
        self._param["camera_list"] = camera_list

        print self._param

        f.close()
