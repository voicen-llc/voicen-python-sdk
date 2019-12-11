from enum import Enum

class PaymentType(Enum):
    PAYMENT = 1
    SUBSCRIPTION = 2

    def to_string(self):
        return self.name.lower()

    @classmethod
    def from_string(cls, payment_type):
        return cls[payment_type.upper()]
