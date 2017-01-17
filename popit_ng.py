import requests


class BaseEntity(object):
    def __init__(self, entity, language="", id=""):
        url = "https://api.popit.sinarproject.org/{language}/{entity}/{id}".format(language=language, id=id, entity=entity)
        r = requests.get(url)
        self.data = r.json()

class Person(BaseEntity):
    def __init__(self, language="", id=""):
        super().__init__("persons", language=language, id=id)
        self.name = self.data["result"]["name"]
