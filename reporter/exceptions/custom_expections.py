class CollectorException(Exception):
    pass

class QueueException(Exception):
    pass

class CouldNotPushMsg(QueueException):
    pass

class CollectorNotFound(CollectorException):
    pass

class AWSCollector(CollectorException):
    pass

class ParseAWSResponseError(AWSCollector):
    pass
