from todo_app.data.card_items import Item
from todo_app.data.view_model import ViewModel


def test_view_model_to_only_return_status_of_to_do():
     #Arrange#
     items = [ 
          Item("card one", "1", "000001", "", "64ef5905b30edf49e85fa346"),
          Item("card two", "2", "000002", "", "64ef5905b30edf49e85fa347"),
          Item("card three", "3", "000003", "", "64ef5905b30edf49e85fa348")
         ]
     view_model = ViewModel(items)

     #Act
     returned_items = view_model.not_started_items

     #Assert
     assert len(returned_items) == 1
     single_item = returned_items[0]
     assert single_item.ListID == "64ef5905b30edf49e85fa346"

def test_view_model_to_only_return_status_of_started_items():
     #Arrange#
     items = [ 
          Item("card one", "1", "000001", "", "64ef5905b30edf49e85fa346"),
          Item("card two", "2", "000002", "", "64ef5905b30edf49e85fa347"),
          Item("card three", "3", "000003", "", "64ef5905b30edf49e85fa348")
         ]
     view_model = ViewModel(items)

     #Act
     returned_items = view_model.started_items
     
     #Assert     
     assert len(returned_items) == 1
     single_item = returned_items[0]
     assert single_item.ListID == "64ef5905b30edf49e85fa347"

def test_view_model_to_move_item_from_todo_to_doing():

     # Arrange
     items = [ 
          Item("card one", "1", "000001", "", "64ef5905b30edf49e85fa346"),
          Item("card tomove", "1.1", "000002", "", "64ef5905b30edf49e85fa346"),
          Item("card two", "2", "000003", "", "64ef5905b30edf49e85fa347"),
          Item("card three", "3", "000004", "", "64ef5905b30edf49e85fa348")
         ]
     view_model = ViewModel(items)

     # Act
     returned_items = view_model.move_item
     
     # Assert
     assert len(returned_items) == 1
     single_item = returned_items[0]
     assert single_item.ID == "000002" and single_item.ListID == "64ef5905b30edf49e85fa347"