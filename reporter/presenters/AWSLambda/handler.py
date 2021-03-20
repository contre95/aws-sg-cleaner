from gateways.collector.collector_factory import RGCollectorFactory
from gateways.queue.queue import Queue
from domain.reporting.reporter import RGReporter
from config import COLLECTORS, SQS_URL, RG_DENYLIST

def lambda_handler(event, context):
    print("Greetings from Reporter Lambda")
    queue = Queue(SQS_URL)
    collectors = [ RGCollectorFactory.get(c) for c in COLLECTORS]
    rgr = RGReporter(queue, collectors, RG_DENYLIST)
    rgr.report_unused_rg()

