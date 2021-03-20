from domain.cleaning.cleaner import  FirewallInterface
from domain.rule_group import RuleGroup

class ExampleFirewall(FirewallInterface):

    __source_key = "example"
    __name = "Example Collector"
    
    def __init__(self):
        pass

    def get_key(self)-> str:
        return ExampleFirewall().__source_key
    
    def get_name(self)-> str:
        return ExampleFirewall().__name


    def delete_group(self, rg:RuleGroup):
        print(f'Deleting rule {rg.name} from {rg.source} on {self.get_name()}')
        pass


