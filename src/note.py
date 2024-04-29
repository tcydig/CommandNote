import flet as ft
from .data_store import DataStore
from .note_stage import NoteStage
from .edit_note_stage import EditNoteStage
class Note(ft.Container):
    def __init__(self,store:DataStore,page:ft.Page):
        super().__init__()
        self.store = store
        self.page = page
        self.padding=10
        self.bgcolor=ft.colors.GREY_400
        self.alignment=ft.alignment.center_left
        self.expand=True

        self.note_content = self.store.getNote()

        if (any(self.note_content)):
            self.title=ft.Text(self.note_content['title'],color=ft.colors.BLACK,size=35,weight=ft.FontWeight.W_600)
            self.summary=ft.Text(self.note_content['summary'],color=ft.colors.BLACK,size=20,weight=ft.FontWeight.W_400)
            self.note_stage=self.create_stage()
            self.content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.IconButton(icon=ft.icons.EDIT_NOTE_OUTLINED,icon_color=ft.colors.BLUE_GREY,on_click=self.edit_note),
                        alignment=ft.alignment.center_left,
                        padding=-10
                    ),
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
                    ft.Container(
                        content=ft.IconButton(icon=ft.icons.EDIT_NOTE_OUTLINED,icon_color=ft.colors.BLUE_GREY,on_click=self.edit_note),
                        alignment=ft.alignment.center_left,
                        padding=-10
                    ),
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
            self.content=ft.Column()
    def add_new_content(self,change_second_menu_function):
        self.change_second_menu_function=change_second_menu_function
        self.title=ft.TextField(label='Title',color=ft.colors.BLACK,bgcolor=ft.colors.WHITE,width=400)
        self.summary=ft.TextField(label='Summary',color=ft.colors.BLACK,bgcolor=ft.colors.WHITE,width=700)
        self.stageList=[EditNoteStage(0,self.store,self.page)]
        self.content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Save", on_click=self.complete_enter),
                        ft.ElevatedButton(text="Cancel", on_click=self.cancel_enter)
                    ]
                ),
                self.title,
                self.summary,
                ft.Container(
                    ft.Column(
                        controls=self.stageList,
                    )
                ),
                ft.Container(
                    ft.IconButton(icon=ft.icons.ADD_CIRCLE,icon_color=ft.colors.BLUE,icon_size=30,on_click=self.add_stage),
                    alignment=ft.alignment.center
                )
            ],
            scroll=ft.ScrollMode.ALWAYS,
            height=1000
        )
        self.page.update()
    def cancel_enter(self,e):
        self.change_content()
        self.page.update()
    def complete_enter(self,e):
        stageList=[{"subTitle":stage.sub_title.value,"cmd":stage.command.value,"description":stage.description.value} for stage in self.stageList]
        self.store.setNewSecondMenu({
            "title":self.title.value,
            "summary":self.summary.value,
            "stage":stageList,
        })
        self.store.setSelectedSecondMenu(self.title.value)
        self.change_second_menu_function()
        self.page.update()
    def add_stage(self,e):
        self.stageList.append(EditNoteStage(len(self.stageList),self.store,self.page))
        self.page.update()
    def edit_note(self,e):
        self.title=ft.TextField(label='Title',color=ft.colors.BLACK,bgcolor=ft.colors.WHITE,width=400,value=self.title.value)
        self.summary=ft.TextField(label='Summary',color=ft.colors.BLACK,bgcolor=ft.colors.WHITE,width=700,value=self.summary.value)
        self.stageList=[EditNoteStage(i,self.store,self.page,self.note_content['stage'][i]) for i in range(len(self.note_content['stage']))]
        self.content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Save", on_click=self.modify_note),
                        ft.ElevatedButton(text="Cancel", on_click=self.cancel_enter)
                    ]
                ),
                self.title,
                self.summary,
                ft.Container(
                    ft.Column(
                        controls=self.stageList,
                    )
                ),
                ft.Container(
                    ft.IconButton(icon=ft.icons.ADD_CIRCLE,icon_color=ft.colors.BLUE,icon_size=30,on_click=self.add_stage),
                    alignment=ft.alignment.center
                )
            ],
            scroll=ft.ScrollMode.ALWAYS,
            height=1000
        )
        self.page.update()
    def modify_note(self,e):
        stageList=[{"subTitle":stage.sub_title.value,"cmd":stage.command.value,"description":stage.description.value} for stage in self.stageList]
        self.store.setModifiedNote({
            "title":self.title.value,
            "summary":self.summary.value,
            "stage":stageList,
        })
        self.change_content()
        self.page.update()