import flet as ft
from .data_store import DataStore

class EditNoteStage(ft.Container):
    def __init__(self,index,store:DataStore,page:ft.Page,initial_value:object={"subTitle":'',"cmd":'',"description":''}):
        super().__init__()
        self.store=store
        self.page=page
        self.index=index

        self.bgcolor=ft.colors.TRANSPARENT


        self.sub_title=ft.TextField(label='subTitle',color=ft.colors.BLACK,bgcolor=ft.colors.WHITE,height=50,value=initial_value['subTitle'])
        self.command=ft.TextField(label='Command',color=ft.colors.WHITE,bgcolor=ft.colors.TRANSPARENT,height=50,value=initial_value['cmd'])
        self.description=ft.TextField(label='Description',multiline=True,max_lines=10,bgcolor=ft.colors.WHITE,color=ft.colors.BLACK,value=initial_value['description'])

        self.content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(f'stage{self.index+1} : ',style=ft.TextStyle(size=15),color=ft.colors.BLACK),
                        self.sub_title
                    ]
                ),
                ft.Container(
                    self.command,
                    width=700,
                    height=50,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center_left,
                ),
                self.description
            ]
        )
