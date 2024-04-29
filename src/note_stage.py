import flet as ft
import subprocess
from .data_store import DataStore

class NoteStage(ft.Container):
    def __init__(self,index,store:DataStore,page:ft.Page):
        super().__init__()
        self.store=store
        self.page=page
        self.index=index

        self.bgcolor=ft.colors.TRANSPARENT

        self.stage = self.store.getStage(self.index)

        self.content=ft.Column(
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan(f'stage{self.index+1} : ',style=ft.TextStyle(size=15)),
                        ft.TextSpan(self.stage['subTitle'],style=ft.TextStyle(size=17))
                    ],
                    color=ft.colors.BLACK,
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                ),
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.icons.CONTENT_COPY,on_click=self.clicked_copy),
                            ft.Text(self.stage['cmd'],color=ft.colors.WHITE,bgcolor=ft.colors.TRANSPARENT,selectable=True),
                        ]  
                    ),
                    width=700,
                    height=50,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center_left,
                ),
                ft.Text(self.stage['description'],color=ft.colors.BLACK)
            ]
        )
    def clicked_copy(self,e):
        subprocess.run("clip", input=self.stage['cmd'], text=True)
