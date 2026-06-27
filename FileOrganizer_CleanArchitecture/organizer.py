from scanner import *
from helper import *
from categorizer import categorize_Files
from folder_manager import create_folders

class FileOrganizer:
    def __init__(self):
        self.path=r"H:\ISO\Project_testOnly"

        self.allFiles=[]
        self.extentions_List=[]
        self.files_category ={}
        self.folder_name_List=[]
        

    def run(self):
        self.allFiles=scan_directory(self.path)
        #print_files(self.allFiles)#for debugging
        self.extentions_List=get_file_extensions(self.allFiles , self.path)
        #print_extentions(self.extentions_List)
        self.files_category = categorize_Files(self.allFiles,self.path)
        #print_dict(self.files_category)
        self.folder_name_List=create_folders(self.extentions_List,self.path)
        print(self.folder_name_List)


        

