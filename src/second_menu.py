import re
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
        self.bgcolor = '#2b2d31'
        self.width = 180
        self.menuList = menuBase.createMenuList(self.store.getSecondMenuList(),self.button_clicked,self.control_delete_button)

        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.IconButton(icon=ft.icons.ADD_BOX,on_click=lambda x: self.note.add_new_content(self.change_content)),
                    alignment=ft.alignment.center_right
                ),
                ft.Column(
                    controls=self.menuList,
                    scroll=ft.ScrollMode.ALWAYS,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START
                )
            ],
            spacing=0
        )

    def button_clicked(self, e):
        # コンテンツ領域の切り替え
        self.store.setSelectedSecondMenu(e.control.data)
        self.note.change_content()
        self.page.update()

        
    def change_content(self,initialSelectedMenu:str=''):
        # 呼び出し元にてself.page.updateを実施
        self.menuList = menuBase.createMenuList(self.store.getSecondMenuList(),self.button_clicked,self.control_delete_button)
        if initialSelectedMenu:
            self.store.setSelectedSecondMenu(initialSelectedMenu)
        else:
            self.store.setSelectedSecondMenu('' if len(self.menuList)==0 else self.menuList[0].data)
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.IconButton(icon=ft.icons.ADD_BOX,on_click=lambda x: self.note.add_new_content(self.add_new_content)),
                    alignment=ft.alignment.center_right
                ),
                ft.Column(
                    controls=self.menuList,
                    scroll=ft.ScrollMode.ALWAYS,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START
                )
            ],
            spacing=0
        )
        self.note.change_content()
    def add_new_content(self):
        # 呼び出し元にてself.page.updateを実施
        self.menuList = menuBase.createMenuList(self.store.getSecondMenuList(),self.button_clicked,self.control_delete_button)
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.IconButton(icon=ft.icons.ADD_BOX,on_click=lambda x: self.note.add_new_content(self.add_new_content)),
                    alignment=ft.alignment.center_right
                ),
                ft.Column(
                    controls=self.menuList,
                    scroll=ft.ScrollMode.ALWAYS,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START
                )
            ],
            spacing=0
        )
        self.note.change_content()
    def control_delete_button(self,e):
        index=0
        for i,v in enumerate(self.menuList):
            if(v.data==e.control.data):
                index=i
                break

        if (e.data=="true"):
            self.menuList[index].content.controls.append(
                ft.Container(
                    ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,icon_size=20,on_click=self.delete_second_menu,data=e.control.data),
                    alignment=ft.alignment.center_right,
                    expand=True
                )
            )
        else:
            self.menuList[index].content.controls.pop()
        
        self.page.update()
    def delete_second_menu(self,e):
        self.store.deleteScondMenu(e.control.data)
        if(self.store.getSelectedSecondMenu()==e.control.data):
            self.change_content(self.store.getSecondMenuList()[0] if len(self.store.getSecondMenuList())>0 else '')
        else:
            self.change_content()
        self.page.update()