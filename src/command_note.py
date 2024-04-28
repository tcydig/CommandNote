import flet as ft
from .data_store import DataStore
from .first_menu import FirstMenu
from .second_menu import SecondMenu
from .note import Note

class CommandNote:
    def __init__(self,page:ft.Page,store:DataStore):
        self.page = page
        self.store = store
        self.note = Note(self.store,self.page)
        self.second_menu = SecondMenu(self.note,self,self.store,self.page)
        self.main_menu = FirstMenu(self,self.second_menu,self.store,self.page)

        self.contentRow = [
            self.main_menu,
            self.second_menu,
            self.note,
        ]
        page.add(
            ft.Row(
                controls=self.contentRow,
                spacing=0,
                expand=True
            )
        )