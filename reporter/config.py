import os
COLLECTORS = os.environ.get("SG_COLLECTORS","example,aws").split(",")
SQS_URL = os.environ.get("SQS_URL")
RG_DENYLIST = set(os.environ.get("RULE_GROUPS_ID_DENYLIST", "sg-1558b14d").split(','))
