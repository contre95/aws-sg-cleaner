from domain.rule_group import RuleGroup
from exceptions.custom_expections import *
from gateways.firewall.aws_firewall import EC2SGFirewall
from gateways.firewall.example_firewall import ExampleFirewall

class FirewallFactory:
    __availale_fw = {"aws": EC2SGFirewall(), "example" : ExampleFirewall()}

    @staticmethod
    def get(firewall_key:str):
        try:
            return FirewallFactory().__availale_fw[firewall_key]
        except KeyError as e:
            print(f"'{firewall_key}' firewall not available")
            raise FirewallNotFound(e)
