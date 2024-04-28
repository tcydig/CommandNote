import flet as ft
from .data_store import DataStore
from .note_stage import NoteStage
class Note(ft.Container):
    def __init__(self,store:DataStore,page:ft.Page):
        super().__init__()
        self.store = store
        self.page = page

        self.bgcolor=ft.colors.GREY_400
        self.padding=30
        self.alignment=ft.alignment.center_left
        self.expand=True

        self.note_content = self.store.getNote()

        if (any(self.note_content)):
            self.title=ft.Text(self.note_content['title'],color=ft.colors.BLACK,size=35,weight=ft.FontWeight.W_600)
            self.summary=ft.Text(self.note_content['summary'],color=ft.colors.BLACK,size=20,weight=ft.FontWeight.W_400)
            self.note_stage=self.create_stage()
            self.content=ft.Column(
                controls=[
                    self.title,
                    self.summary,
                    ft.Container(
                        ft.Column(
                            controls=self.note_stage
                        )
                    )
                ]
            )
        else:
            pass
    def create_stage(self):
        return [NoteStage(i,self.store,self.page) for i in range(len(self.note_content['stage'])) ]
    def change_content(self):
        self.note_content=self.store.getNote()

        if (any(self.note_content)):
            self.title=ft.Text(self.note_content['title'],color=ft.colors.BLACK,size=35,weight=ft.FontWeight.W_600)
            self.summary=ft.Text(self.note_content['summary'],color=ft.colors.BLACK,size=20,weight=ft.FontWeight.W_400)
            self.note_stage=self.create_stage()
            
            self.content=ft.Column(
                controls=[
                    self.title,
                    self.summary,
                    ft.Container(
                        ft.Column(
                            controls=self.note_stage
                        )
                    )
                ]
            )
        else:
            pass
