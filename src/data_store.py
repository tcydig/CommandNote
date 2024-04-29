import os
import json
class DataStore():
    def __init__(self):
        self.dir_path=os.getenv('LOCALAPPDATA')+'\\CommandNote'
        self.file_name='store.json'
        try:
            self.getStoreJson()
        except:
            self.createAppLocalFolder()
            self.getStoreJson()
        self.selected_first_menu = '' if len(self.getFirstMenuList())==0 else self.getFirstMenuList()[0]
        self.selected_second_menu = '' if len(self.getSecondMenuList())==0 else self.getSecondMenuList()[0]

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
        if (self.getSelectedFirstMenu() in self.original_store):
            return [key for key in self.original_store[self.getSelectedFirstMenu()].keys()]
        else:
            return []
    def getNote(self):
        if (self.getSelectedFirstMenu() in self.original_store and self.getSelectedSecondMenu() in self.original_store[self.getSelectedFirstMenu()]):
            return self.original_store[self.getSelectedFirstMenu()][self.getSelectedSecondMenu()]
        else:
            return {}
    def getStage(self,index):
        return self.original_store[self.getSelectedFirstMenu()][self.getSelectedSecondMenu()]['stage'][index]
    
    def createAppLocalFolder(self):
        try:
            os.makedirs(self.dir_path, exist_ok=True)
            with open(f'{self.dir_path}\\{self.file_name}','w') as file:
                json.dump({}, file)
        except Exception as e:
            print(f'エラーが発生しました: {e}')
    def getStoreJson(self):
        with open(f'{self.dir_path}\\{self.file_name}',encoding="utf-8") as json_file:
            self.original_store = json.load(json_file)
    def setNewFirstMenu(self,value):
        if (value in self.original_store): return
        self.original_store[value]={}
        try:
            with open(f'{self.dir_path}\\{self.file_name}', 'w',encoding="utf-8") as file:
                json.dump(self.original_store, file, indent=4)
            self.getStoreJson()
        except Exception as e:
            print(f'エラーが発生しました: {e}')

