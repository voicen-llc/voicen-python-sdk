from .subscription_status import SubscriptionStatus

class Subscription:
    def __init__(self,
                 created_on,
                 expires_on,
                 status):
        """
        :param created_on: the date and time subscription starts
        :param expires_on: the date and time subscription ends
        :param status: status of subscription. Can be one of: ACTIVE, EXPIRED, SUSPENDED, CANCELLED, TERMINATED
        """

        self.created_on = created_on
        self.expires_on = expires_on
        self.status = status

    def dump_json(self):
        json_desc = '{\n'
        json_desc += '\t\"created_on\": \"' + self.created_on + '\",\n'
        json_desc += '\t\"expires_on\": \"' + self.expires_on + '\",\n'
        json_desc += '\t\"status\": \"' + self.status.to_string() + '\"\n'
        json_desc += '}'
        return json_desc

    @classmethod
    def parse_json(cls, json):
        """Creates instance from json description of subscription"""
        if(json is None):
            return None

        return cls(
            json["createdOn"],
            json["expiresOn"],
            SubscriptionStatus.from_string(json["status"])
        )

