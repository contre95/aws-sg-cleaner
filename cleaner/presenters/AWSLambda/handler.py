from gateways.firewall.firewall_factory import FirewallFactory
from mappers.sqs import SQSRuleGroupMapper
from domain.cleaning.cleaner import Cleaner
from config import FIREWALLS

def lambda_handler(event, context):
    print("Hello from Lambda Cleaner")
    rg = SQSRuleGroupMapper.map(event)
    firewall = FirewallFactory.get(rg.get_source())
    cleaner = Cleaner(firewall, rg)
    cleaner.clean()
    
    # Instanciar un ALGOQUEMEDERG + FIREWALL
    # Pasarselo a mi UseCase CLEANER

    # queue = Queue()
    # firewall = [ FirewallFactory.get(f) for f in FIREWALLS]
    # rule_groups_cleaner = SGReporter(queue, collectors)
    # sgr.rerport_unused_sg()
    # LOGGER.info("%s", pformat({"Context" : vars(context), "Request": event}))
    # return response(status=200, body=event['body'])


