class Account:
    def __init__(self,
                 email,
                 balance_seconds):
        """
        :param email: email of account
        :param balance_seconds: balance of account in seconds
        """
        self.email = email
        self.balance_seconds = balance_seconds

    def dump_json(self):
        json_desc = '{\n'
        json_desc += '\t\"email\": \"' + self.email + '\",\n'
        json_desc += '\t\"balance_seconds\": ' + str(self.balance_seconds) + '\n'
        json_desc += '}'
        return json_desc

    @classmethod
    def parse_json(cls, json):
        """Creates instance from JSON description of account"""
        return cls(
            json["email"],
            json["balanceInSeconds"]
        )
