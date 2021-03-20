from domain.cleaning.cleaner import RuleGroupMapper
from domain.rule_group import RuleGroup
from exceptions.custom_expections import CouldNotMapLambdaEvent


class SQSRuleGroupMapper(RuleGroupMapper):

    @staticmethod
    def map(lambda_event)-> 'RuleGroup':
        try:
            msg = lambda_event['Records'][0]
            msg_attr = msg['messageAttributes']
            rg = RuleGroup(msg_attr['Name']['stringValue'],msg['body'],msg_attr['Source']['stringValue'])
            return rg
        except Exception as e:
            raise CouldNotMapLambdaEvent(f"Could not parse lambda evento into RuleGroup : {e}")
