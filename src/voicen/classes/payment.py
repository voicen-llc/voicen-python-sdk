from .payment_type import PaymentType
from .subscription import Subscription

class Payment:
    def __init__(self,
                 transaction_id,
                 amount,
                 type,
                 purchased_minutes,
                 created,
                 subscription):
        """
        :param transaction_id: transaction ID of payment
        :param amount: payment amount
        :param payment_type: type of payment. Can be one of: PAYMENT, SUBSCRIPTION
        :param purchased_minutes: purchased transcribing time in minutes
        :param created: date and time of payment
        :param subscription: if payment type is SUBSCRIPTION this field will not none.
        """

        self.transaction_id = transaction_id
        self.amount = amount
        self.type = type
        self.purchased_minutes = purchased_minutes
        self.created = created
        self.subscription = subscription

    def dump_json(self):
        json_desc = '{\n'
        json_desc += '\t\"transaction_id\": \"' + self.transaction_id + '\",\n'
        json_desc += '\t\"amount\": ' + str(self.amount) + ',\n'
        json_desc += '\t\"type\": \"' + self.type.to_string() + '\",\n'
        json_desc += '\t\"purchased_minutes\": ' + str(self.purchased_minutes) + ',\n'
        json_desc += '\t\"created\": \"' + self.created + '\"'
        if self.subscription is not None:
            json_desc += ',\n\t\"subscription\": '
            subscr_json = self.subscription.dump_json()
            subscr_json_lines = subscr_json.split('\n')
            for line in subscr_json_lines:
                if line != subscr_json_lines[0] and line != subscr_json_lines[-1]:
                    json_desc += '\t\t'
                if line == subscr_json_lines[-1]:
                    json_desc += '\t'
                json_desc += line
                json_desc += '\n'
        else:
            json_desc += '\n'
        json_desc += '}'
        return json_desc

    @classmethod
    def parse_json(cls, json):
        return cls(
            json["transactionId"],
            json["amount"],
            PaymentType.from_string(json["type"]),
            json.get("purchasedMinutes"),
            json.get("created"),
            Subscription.parse_json(json.get("subscription"))
        )
