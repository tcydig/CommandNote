import flet as ft
from .data_store import DataStore

class EditNoteStage(ft.Container):
    def __init__(self,index,note,store:DataStore,page:ft.Page,initial_value:object={"subTitle":'',"cmd":'',"description":''}):
        super().__init__()
        self.store=store
        self.page=page
        self.index=index
        self.note=note

        self.bgcolor=ft.colors.TRANSPARENT


        self.sub_title=ft.TextField(
            label='SubTitle',
            color=ft.colors.WHITE,
            bgcolor='#383a40',
            border=ft.InputBorder.UNDERLINE,
            filled=True,
            value=initial_value['subTitle']
            )
        self.command=ft.TextField(
            label='Command',
            color=ft.colors.WHITE,
            bgcolor=ft.colors.TRANSPARENT,
            height=50,
            value=initial_value['cmd']
        )
        self.description=ft.TextField(
            label='Description',
            multiline=True,
            max_lines=10,
            bgcolor='#383a40',
            border=ft.InputBorder.UNDERLINE,
            color=ft.colors.WHITE,
            value=initial_value['description']
        )

        self.content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(f'stage{self.index+1} : ',style=ft.TextStyle(size=15),color=ft.colors.WHITE),
                        self.sub_title,
                        ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=lambda x: self.note.delete_stage(index))
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
