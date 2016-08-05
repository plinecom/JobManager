from jsonpath_rw import jsonpath, parse


class ConfigInfo:
    def __init__(self, config_list):
        self._configlist = config_list

    def getvalue_by_json_path(self, json_path):
        jsonpath_expr = parse(json_path)
#        print jsonpath
#        print [match.value for match in jsonpath_expr.find(self._configlist)]
        return [match.value for match in jsonpath_expr.find(self._configlist)]
