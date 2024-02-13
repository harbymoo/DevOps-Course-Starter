from todo_app.data.card_items import Item

class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items


    @property
    def items(self):
        return self._items
    
    @property
    def not_started_items(self):
        output_list = []

        for item in self._items:
            if item.ListID == "64ef5905b30edf49e85fa346":
                output_list.append(item)
            
        return output_list
    
    @property
    def started_items(self):
        output_list = []

        for item in self._items:
            if item.ListID == "64ef5905b30edf49e85fa347":
                output_list.append(item)
            
        return output_list
    
    @property
    def move_item(self):
        output_list = []

        for item in self._items:
            if item.ID == "000002":
                item.ListID = '64ef5905b30edf49e85fa347'
                print(item)
                output_list.append(item)
            
        return output_list