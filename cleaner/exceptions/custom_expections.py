class FirewallError(Exception):
    pass
class FirewallNotFound(FirewallError):
    pass
class CouldNotDeleteRuleGroup(FirewallError):
    pass
class MapperError(Exception):
    pass
class CouldNotMapLambdaEvent(MapperError):
    pass

