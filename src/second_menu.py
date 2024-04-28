import flet as ft
from .data_store import DataStore
from .menu_base import menuBase
from .note import Note
class SecondMenu(ft.Container,menuBase):
    def __init__(self,note:Note,command_note,store:DataStore,page):
        super().__init__()
        self.note = note
        self.command_note = command_note
        self.store:DataStore = store
        self.page = page
        self.bgcolor = ft.colors.BLUE_GREY_600
        self.width = 150
        menuList = menuBase.createMenuList(self.store.getSecondMenuList(),self.button_clicked)

        self.content = ft.Column(
            controls=menuList,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
    def button_clicked(self, e):
        # コンテンツ領域の切り替え
        self.store.setSelectedSecondMenu(e.control.data)
        self.note.change_content()
        self.page.update()

        
    def change_content(self):
        # 呼び出し元にてself.page.updateを実施
        menuList = menuBase.createMenuList(self.store.getSecondMenuList(),self.button_clicked)
        self.store.setSelectedSecondMenu(menuList[0].data)
        self.content = ft.Column(
            controls=menuList,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
        self.note.change_content()
