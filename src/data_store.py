import os
import json
class DataStore():
    def __init__(self):    
        with open(os.path.dirname(os.path.realpath(__file__)) + '\store.json',encoding="utf-8") as json_file:
            self.original_store = json.load(json_file)
        self.selected_first_menu = self.getFirstMenuList()[0]
        self.selected_second_menu = self.getSecondMenuList()[0]

    def getSelectedFirstMenu(self):
        return self.selected_first_menu
    def setSelectedFirstMenu(self,value):
        self.selected_first_menu = value
    def getSelectedSecondMenu(self):
        return self.selected_second_menu
    def setSelectedSecondMenu(self,value):
        self.selected_second_menu = value

    def getFirstMenuList(self):
        return [key for key in self.original_store.keys()]
    def getSecondMenuList(self):
        return [key for key in self.original_store[self.getSelectedFirstMenu()].keys()]
    def getNote(self):
        return self.original_store[self.getSelectedFirstMenu()][self.getSelectedSecondMenu()]
    def getStage(self,index):
        return self.original_store[self.getSelectedFirstMenu()][self.getSelectedSecondMenu()]['stage'][index]