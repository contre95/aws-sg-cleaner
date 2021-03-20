
class RuleGroup():

    def __init__(self, name:str, uid:str, source_key:str):
        self.uid = uid
        self.name = name
        self.source = source_key

    def get_id (self)->str:
        return self.uid

    def get_name(self)->str:
        return self.name

    def get_source(self)->str:
        return self.source

class SecurityGroup(RuleGroup):
    
    def set_arn(self, arn:str):
        self.arn = arn

    def get_arn(self)->str:
        if self.arn:
            return self.arn

