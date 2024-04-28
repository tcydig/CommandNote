import flet as ft
from .data_store import DataStore
from .second_menu import SecondMenu
from .menu_base import menuBase

class FirstMenu(ft.Container,menuBase):
    def __init__(self,command_note,second_menu:SecondMenu,store:DataStore,page):
        super().__init__()
        self.command_note = command_note
        self.second_menu:SecondMenu = second_menu
        self.store:DataStore = store
        self.page = page
        self.bgcolor = ft.colors.BLUE_GREY_800
        self.width = 150

        self.menuList = menuBase.createMenuList(self.store.getFirstMenuList(),self.button_clicked)

        self.content = ft.Column(
            controls=self.menuList,
        )
    def button_clicked(self, e):
        self.store.setSelectedFirstMenu(e.control.data)
        self.second_menu.change_content()
        self.page.update()