from abc import ABC, abstractmethod
from domain.rule_group import RuleGroup


class FirewallInterface(ABC):
    
    @abstractmethod
    def delete_group(self, rg:RuleGroup):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

class RuleGroupMapper(ABC):

    @abstractmethod
    def map(data) -> 'RuleGroup':
        pass

class Cleaner:

    def __init__(self, fw, rg):
        self.rule_group = rg
        self.firewall = fw

    def clean(self):
            print(f"Cleaning {self.rule_group.get_name()} ({self.rule_group.get_id()}) from {self.rule_group.get_source()}")
            # Check blacklist
            self.firewall.delete_group(self.rule_group)

