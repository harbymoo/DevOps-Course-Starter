class Item:
    def __init__(self, name, DESC, ID, due, ListID):
        self.name = name
        self.DESC = DESC
        self.ID = ID
        self.due = due
        self.ListID = ListID

    @classmethod
    def from_list_dictionaries(cls, item):
        return cls(item['name'], item['DESC'], item['ID'], item['due'], item['ListID'])