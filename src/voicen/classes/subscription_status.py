from enum import Enum

class SubscriptionStatus(Enum):
    ACTIVE = 1
    EXPIRED = 2
    SUSPENDED = 3
    CANCELLED = 4
    TERMINATED = 5

    def to_string(self):
        return self.name.lower()

    @classmethod
    def from_string(cls, status):
        return cls[status.upper()]
