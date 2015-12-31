from jsonpath_rw import jsonpath, parse

class ConfigInfo:
    def __init__(self, configList):
        self._configlist = configList

    def getvalue(self,key):
        dic={}
        for config_doc in self._configlist:
#          print config_doc
            for config_title in config_doc.keys():
                if config_doc[config_title].has_key(key):
                    value = config_doc[config_title][key]
                    #print value
                    if isinstance(value, unicode):
                        return value.encode('utf-8')
                    if isinstance(value,dict):
                        dic.update(value)
                    else:
                        return value
        if len(dic.keys()) > 0:
            return dic
        else:
            return None
    def getparam(self):
        return self._configlist

    def _getvalue_recursive(self, elements, keyPathList):

        if isinstance(elements,list):
            for element in elements:
                if(isinstance(element,list)) or isinstance(element, dict):
                    pass


    def getvalueJsonPath(self,jsonpath):
        jsonpath_expr = parse(jsonpath)
        print jsonpath
        print [match.value for match in jsonpath_expr.find( self._configlist)]




    def getvaluepath(self,keypath):

        elements = self._configlist

        keypathList = str(keypath).split('/')
        while keypathList.count("") > 0: keypathList.remove("")

        self._getvalue_recursive(elements, keypathList)
