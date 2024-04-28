import flet as ft
from src.data_store import DataStore
from src.command_note import CommandNote

def main(page: ft.Page):
    page.title = 'command note'
    CommandNote(page,DataStore())

ft.app(target=main)