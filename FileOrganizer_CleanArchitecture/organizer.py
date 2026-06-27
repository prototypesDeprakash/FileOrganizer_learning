from scanner import *
from helper import *

class FileOrganizer:
    def __init__(self):
        self.path=r"H:\ISO\Project_testOnly"

        self.allFiles=[]
        self.extentions_List=[]

    def run(self):
        self.allFiles=scan_directory(self.path)
        print_files(self.allFiles)#for debugging
        self.extentions_List=get_file_extensions(self.allFiles , self.path)
        print_extentions(self.extentions_List)
        

