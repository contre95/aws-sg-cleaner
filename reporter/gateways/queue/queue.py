from domain.reporting.reporter import QueueInterface
from gateways.queue.sqs import SQS

class Queue(QueueInterface):

    def __new__(cls, *args, **kwargs):
        return SQS(*args)


