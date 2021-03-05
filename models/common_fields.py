'''
CommonFields Object Description:
    {
      "id": int,
      "name": "string",
      "label": "string",
      "description": "string",
      "info":	{}
    }
'''
class CommonFields:
    def __init__(self, name: str, label: str, cf_id=0, description="", info={}):
        self.cf_id=cf_id
        self.name = name
        self.label = label
        self.description = description
        self.info= info
    
    def __str__(self):
        result = "{\n\t"
        result += "id: "+str(self.cf_id)+"\n\t"   
        result += "name: "+self.name+"\n\t"   
        result += "label: "+self.label+"\n\t"   
        result += "description: "+self.description+"\n\t"
        result += "}\n\t"
        return result
