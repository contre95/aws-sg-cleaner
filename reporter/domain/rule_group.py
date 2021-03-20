from dataclasses import dataclass

@dataclass
class RuleGroup():
    name:str
    uid:str
    source:str

    def __init__(self, name:str, uid:str, source_key:str):
        self.name = name
        self.source =  source_key
        self.uid = uid

    def get_id (self)->str:
        return self.uid

    def get_name(self)->str:
        return self.name

    def get_source(self)->str:
        return self.source

    def __eq__(self, other):
        return self.uid == self.uid
    
    def __hash__(self):
        return hash(str(self.uid+self.name))


class SecurityGroup(RuleGroup):
    
    def set_arn(self, arn:str):
        self.arn = arn

    def get_arn(self)->str:
        if self.arn:
            return self.arn
