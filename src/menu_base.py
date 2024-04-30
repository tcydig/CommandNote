import flet as ft
class menuBase():
    def __init__(self):
        pass
    def createMenuList(targetList,callbackFunction,deleteButtonFunction):
        return [
            ft.TextButton(
                content=ft.Row(
                    [
                        ft.Text(text,text_align=ft.alignment.center_left)
                    ]
                ),
                on_click=callbackFunction,
                data=text,
                # width=200,
                on_hover=deleteButtonFunction,
                style=ft.ButtonStyle(color=ft.colors.WHITE),
            ) 
            for text in targetList
        ]