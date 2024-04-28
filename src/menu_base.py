import flet as ft
class menuBase():
    def createMenuList(targetList,callbackFunction):
        return [
            ft.TextButton(
                content=ft.Row(
                    [
                        ft.Text(text,text_align=ft.alignment.center_left)
                    ]
                ),
                on_click=callbackFunction,
                data=text,
                width=200,
                style=ft.ButtonStyle(color=ft.colors.WHITE)
            ) 
            for text in targetList
        ]