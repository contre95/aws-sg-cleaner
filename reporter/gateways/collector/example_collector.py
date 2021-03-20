from domain.reporting.reporter import RGCollectorInterface
from domain.rule_group import RuleGroup

class ExampleCollector(RGCollectorInterface):
    
    __key = "example"
    __name = "Example Collector"


    def get_name(self)->str:
        return ExampleCollector().__name 

    def get_key(self):
        return  ExampleCollector().__key 

    def get_unused_rule_groups(self) -> list:
        rg_1 = RuleGroup("ExmpleRG", "rg-1234567", self.get_key())
        return [rg_1]
