from domain.reporting.reporter import RGCollectorInterface
from domain.rule_group import SecurityGroup
from exceptions.custom_expections import ParseAWSResponseError
import boto3

class AWSSGCollector(RGCollectorInterface):
    __source_key = "aws"
    __name = "AWS SecurityGroup Collector"
    
    def __init__(self):
        self.client = boto3.client('ec2')


    def _token_handler(self, callback, next_token=None):
        if next_token:
            resp = callback(
                    NextToken = next_token,
                    MaxResults= 100
                    )
        else:
            resp = callback()
        return resp

    def _take_sgs_from_enis(self, enis_set:set, enis:list):
        for eni in enis:
           for sg in eni['Groups']:
                enis_set.add(SecurityGroup(sg['GroupName'], sg['GroupId'], self.get_key()))

    def _get_network_interfaces_sgs(self)->set:
        # resp = self.client.describe_network_interfaces()
        enis_sgs = set()
        done, token = False, None
        try:
            while done == False:
                resp = self._token_handler(self.client.describe_network_interfaces,token)
                self._take_sgs_from_enis(enis_sgs, resp['NetworkInterfaces']) 
                if 'NextToken' in resp:
                    token = resp['NextToken']
                else:
                    done = True
            return enis_sgs
        except Exception as e:
            print(f"ParseAWSResponseError: Could not parse AWS describe_network_interfaces response into Rule Groups: {e}")
            raise ParseAWSResponseError(e)
    
    def _get_security_groups(self)-> list:
        # resp = self.client.describe_security_groups()
        done, token = False, None
        sgs = []
        try:
            while done == False:
                resp = self._token_handler(self.client.describe_security_groups,token)
                sgs += [SecurityGroup(sg["GroupName"], sg["GroupId"], self.get_key()) for sg in resp['SecurityGroups'] ]
                if 'NextToken' in resp:
                    token = resp['NextToken']
                else:
                    done = True  
            return sgs
        except Exception as e:
            print(f"ParseAWSResponseError: Could not parse AWS describe_security_groups response into Rule Groups: {e}")
            raise ParseAWSResponseError(e)

    def get_key(self)-> str:
        return AWSSGCollector().__source_key
    
    def get_name(self)-> str:
        return AWSSGCollector().__name

    def get_unused_rule_groups(self)->list:
        unused_sgs = []
        used_sgs = self._get_network_interfaces_sgs()
        all_sgs = self._get_security_groups()
        for sg in all_sgs:
            if sg not in used_sgs:
                unused_sgs.append(sg)
        return unused_sgs

    
