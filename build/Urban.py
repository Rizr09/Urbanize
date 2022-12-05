import requests as r

class Urban:
    def __init__(self) -> None:
        self._word = None
        self._data = None
    
    def setWord(self, word):
        self._word = word

    def getWord(self):
        return self._word

    def setData(self, data):
        self._data = data

    def getData(self):
        return self._data

    def parser(self):
        special_char = (
            ("%", "%25"),
            (" ", "%20"),
            (",", "%2C"),
            ("?", "%3F"),
            ("\n", "%0A"),
            ('\"', "%22"),
            ("<", "%3C"),
            (">", "%3E"),
            ("#", "%23"),
            ("|", "%7C"),
            ("&", "%26"),
            ("=", "%3D"),
            ("@", "%40"),
            ("#", "%23"),
            ("$", "%24"),
            ("^", "%5E"),
            ("`", "%60"),
            ("+", "%2B"),
            ("\'", "%27"),
            ("{", "%7B"),
            ("}", "%7D"),
            ("[", "%5B"),
            ("]", "%5D"),
            ("/", "%2F"),
            ("\\", "%5C"),
            (":", "%3A"),
            (";", "%3B")
        )
        for word in special_char:
            self.setWord(self.getWord().replace(*word))

    def request(self):
        self.parser()
        url = f"http://api.urbandictionary.com/v0/define?term={self.getWord()}"
        self.setData(r.get(url).json())

    def definition(self):
        self.request()
        return self.getData()["list"][0]["definition"]
    
    def main(self):
        self.setWord(input("Word: "))
        print(self.definition())