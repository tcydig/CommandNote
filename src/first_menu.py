import re
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
        self.width = 180

        self.menuList = menuBase.createMenuList(self.store.getFirstMenuList(),self.button_clicked)

        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.IconButton(icon=ft.icons.ADD_BOX,on_click=self.add_content),
                    alignment=ft.alignment.center_right
                ),
                ft.Column(
                    controls=self.menuList,
                )
            ],
            spacing=0
        )

    def button_clicked(self, e):
        self.store.setSelectedFirstMenu(e.control.data)
        self.second_menu.change_content()
        self.page.update()
    def add_content(self, e):
        if(len(self.content.controls)==3):return
        self.content.controls.extend(
            [
                ft.TextField(label="Enter text",bgcolor=ft.colors.WHITE,border=ft.InputBorder.NONE,filled=True,hint_text="Enter text",color=ft.colors.BLACK),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Save", on_click=self.complete_enter),
                        ft.ElevatedButton(text="Cancel", on_click=self.cancel_enter)
                    ]
                )
            ]
        )
        self.page.update()
    def complete_enter(self,e):
        value = self.content.controls[2].value
        if (re.search('\\S',value)):
            self.store.setNewFirstMenu(value)
            self.hide_input_area()
        else:
            self.hide_input_area()
            self.page.update()
            return
        self.getFirstMenu()
        self.store.setSelectedFirstMenu(value)
        self.second_menu.change_content()
        self.page.update()
        
    def cancel_enter(self,e):
        if(len(self.content.controls)==2):return
        self.hide_input_area()
        self.page.update()
    def hide_input_area(self):
        self.content.controls=self.content.controls[:2]
    def getFirstMenu(self):
        self.menuList = menuBase.createMenuList(self.store.getFirstMenuList(),self.button_clicked)

        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.IconButton(icon=ft.icons.ADD_BOX,on_click=self.add_content),
                    alignment=ft.alignment.center_right
                ),
                ft.Column(
                    controls=self.menuList,
                )
            ],
            spacing=0
        )