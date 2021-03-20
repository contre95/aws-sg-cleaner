from abc import ABC, abstractmethod
from domain.rule_group import RuleGroup

class QueueInterface(ABC):

    @abstractmethod
    def push(self, rg:RuleGroup):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

class RGCollectorInterface(ABC):

    @abstractmethod
    def get_unused_rule_groups(self) -> list:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_key(self) -> str:
        pass


class RGReporter:

    def __init__(self, rg_queue, rg_collectors, rg_deny_list):
        self.queue = rg_queue
        self.collectors = rg_collectors
        self.rg_deny_list = rg_deny_list

    def _get_rgs(self)->list:
        rule_groups = []
        for collector in self.collectors:
            unused_rgs = collector.get_unused_rule_groups()
            for rg in unused_rgs:
                rule_groups.append(rg)
        return rule_groups

    def report_unused_rg(self):
        rule_groups = self._get_rgs()
        for rg in rule_groups:
            if rg.get_id() not in self.rg_deny_list:
                self.queue.push(rg)
            else:
                print(f"Skipping {rg.get_name()} rule group ({rg.get_id()}) since it's denied")

