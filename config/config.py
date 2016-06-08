from jsonpath_rw import jsonpath, parse

class ConfigInfo:
    def __init__(self, configList):
        self._configlist = configList




    def getvalueJsonPath(self,jsonpath):
        jsonpath_expr = parse(jsonpath)
        print jsonpath
        print [match.value for match in jsonpath_expr.find( self._configlist)]
        return [match.value for match in jsonpath_expr.find( self._configlist)]


