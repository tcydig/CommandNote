import flet as ft
from .data_store import DataStore

class NoteStage(ft.Container):
    def __init__(self,index,store:DataStore,page:ft.Page):
        super().__init__()
        self.store=store
        self.page=page
        self.index=index


        self.width=600
        self.bgcolor=ft.colors.TRANSPARENT

        self.stage = self.store.getStage(self.index)

        self.content=ft.Column(
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan(f'stage{self.index+1} : '),
                        ft.TextSpan(self.stage['subTitle'])
                    ],
                    color=ft.colors.BLACK,
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                ),
                ft.Container(
                  content=ft.Text(self.stage['cmd'],color=ft.colors.WHITE,bgcolor=ft.colors.TRANSPARENT,selectable=True),
                  width=500,
                  height=50,
                  bgcolor=ft.colors.BLACK,
                  alignment=ft.alignment.center_left,
                ),
                ft.Text(self.stage['description'],color=ft.colors.BLACK)
            ]
        )
