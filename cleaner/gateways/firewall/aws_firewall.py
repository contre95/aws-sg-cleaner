from domain.cleaning.cleaner import  FirewallInterface
from domain.rule_group import SecurityGroup
from exceptions.custom_expections import CouldNotDeleteRuleGroup
import boto3

class EC2SGFirewall(FirewallInterface):
    __name = "EC2SG"

    def __init__(self):
        self.client = boto3.client('ec2')
    
    def delete_group(self, sg:SecurityGroup):
        try:
            resp = self.client.delete_security_group(GroupId=sg.get_id())
        except Exception as e:
            print(f"CouldNotDeleteRuleGroup: There was an error when calling detele_security_group function: {e}")
            raise  CouldNotDeleteRuleGroup(e)
        pass

    def get_name(self):
        return "Example Firewall"
