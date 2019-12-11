from .word import Word

class Transcription:
    def __init__(self, text = "", words = []):
        """
        :param text: text of transcription
        :param words: detailed words of transcription
        """
        self.text = text
        self.words = words

    def dump_json(self):
        json_desc = '{\n'
        json_desc += '\t\"text\": \"' + self.text + '\",\n'
        json_desc += '\t\"words\": [\n'
        for word in self.words:
            word_json = word.dump_json()
            word_json_lines = word_json.split('\n')
            for line in word_json_lines:
                json_desc += '\t\t' + line
                if line != word_json_lines[-1]:
                    json_desc += '\n'
            if word != self.words[-1]:
                json_desc += ','
            json_desc += '\n'
        json_desc += '\t]\n'
        json_desc += '}'
        return json_desc

    @classmethod
    def parse_json(cls, json):
        """JSON description of transcription"""
        return cls(
            json["fulltext"],
            [Word.parse_json(word) for word in json["words"]]
        )
