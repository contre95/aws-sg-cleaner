from domain.rule_group import RuleGroup
from exceptions.custom_expections import *
from gateways.collector.aws_collector import AWSSGCollector
from gateways.collector.example_collector import ExampleCollector

class RGCollectorFactory:
    __availale_deniers = {"aws": AWSSGCollector(), "example" : ExampleCollector()}

    @staticmethod
    def get(Collector:str):
        try:
            return RGCollectorFactory().__availale_deniers[Collector]
        except KeyError as e:
            print("Collector not available")
            raise CollectorNotFound(e)
