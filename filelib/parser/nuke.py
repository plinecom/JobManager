import abstract


__author__ = 'Masataka'


class FileParserNuke(abstract.FileParserBase):
    def __init__(self, file_path):
        abstract.FileParserBase.__init__(self, file_path)
        self._param["software"] = "Nuke"

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

        root_parse = False
        write_parse = False
        for l in f:
            # print l
            if version is None and 'version' in l:
                temp = l
                version = temp.split()[1]
                minor_version = temp.split()[2]
                print version
                print minor_version
            if "Root {" in l:
                root_parse = True

            if root_parse:
                if frame_start is None and " frame" in l:
                    temp = l
                    frame_start = temp.split()[1]
                    print frame_start
            if frame_end is None and " last_frame" in l:
                temp = l
                frame_end = temp.split()[1]
                print frame_end

            if "}" in l:
                root_parse = False
                write_parse = False


        if renderer is None:
            renderer = 'file'
        # print renderer
        # print renderlayer_enable
        if frame_start is None:
            frame_start = "1"
        if frame_end is None:
            frame_end = str(int(frame_start) + 9)
        if by_frame_steps is None:
            by_frame_steps = "0"

        self._param["filePath"] = self.get_file_path()
        self._param["version"] = version
        self._param["application"] = "Maya_" + version
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
