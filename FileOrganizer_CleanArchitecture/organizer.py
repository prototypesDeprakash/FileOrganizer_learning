from scanner import *
from helper import *
from categorizer import categorize_Files
from folder_manager import create_folders
from mover import move_files
from summary import create_summary

class FileOrganizer:
    def __init__(self):
        self.path=r""

        self.allFiles=[]
        self.extentions_List=[]
        self.files_category ={}
        self.folder_name_List=[]
        self.summary_list = []
        

    def run(self,userpath):
        
        self.path=userpath
        print(self.path)
        self.allFiles=scan_directory(self.path)
        self.extentions_List=get_file_extensions(self.allFiles , self.path)
        self.files_category = categorize_Files(self.allFiles,self.path)
        self.folder_name_List=create_folders(self.extentions_List,self.path)
        move_files(self.files_category,self.path)
        self.summary_list = create_summary(self.files_category,self.folder_name_List)


        

