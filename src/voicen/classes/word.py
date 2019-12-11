class Word:
    def __init__(self,
                 word,
                 start_time,
                 end_time,
                 confidence):
        """
        :param word: any word in transcription
        :param start_time: start time of word in milliseconds
        :param end_time: end time of word in milliseconds
        :param confidence: confidence score of word
        """
        self.word = word
        self.start_time = start_time
        self.end_time = end_time
        self.confidence = confidence

    def dump_json(self):
        json_desc = '{\n'
        json_desc += '\t\"word\": \"' + self.word + '\",\n'
        json_desc += '\t\"start_time\": ' + str(self.start_time) + ',\n'
        json_desc += '\t\"end_time\": ' + str(self.end_time) + ',\n'
        json_desc += '\t\"confidence\": ' + str(self.confidence) + '\n'
        json_desc += '}'
        return json_desc

    @classmethod
    def parse_json(cls, json):
        """Creates instance from JSON description of word"""
        return cls(
            json["word"],
            json["startTime"],
            json["endTime"],
            json["confidence"]
        )
