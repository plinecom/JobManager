class ConfigInfo:
    def __init__(self, configList):
        self._configlist = configList

    def getvalue(self,key):
        for config_doc in self._configlist:
#          print config_doc
            for config_title in config_doc.keys():
                if config_doc[config_title].has_key(key):
                    value = config_doc[config_title][key]
                    #print value
                    if isinstance(value, unicode):
                        return value.encode('utf-8')
                    else:
                        return value
        return None
