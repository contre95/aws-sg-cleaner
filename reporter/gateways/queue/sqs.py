from domain.reporting.reporter import QueueInterface
from exceptions.custom_expections import CouldNotPushMsg
from config import SQS_URL
from domain.rule_group import RuleGroup
from dataclasses import asdict
import boto3, json

class SQS(QueueInterface):
    __name = "AWS SQS Queue"

    def __init__(self, url):
        self.url = url
        self.client = boto3.client("sqs") 

    def get_name(self):
        return SQS(self.url).__name

    def push(self, rg:RuleGroup):
        try:
            print(f'Pushin RG {rg.name} with id {rg.uid} from {rg.get_source()} to queue {self.get_name()}')
            self.client.send_message(
                    QueueUrl = self.url,
                    MessageBody = f"{rg.get_id()}",
                    DelaySeconds = 3,
                    MessageAttributes={
                        "Name" : {
                            "DataType" : "String",
                            "StringValue" : f"{rg.get_name()}"
                            },
                        "Source" : {
                            "DataType": "String",
                            "StringValue": f"{rg.get_source()}"
                            }                                
                        })
        except Exception as e:
            print(f"Couldn't push SecurityGroup {rg.name} : {e} ")
            raise CouldNotPushMsg(e) 

