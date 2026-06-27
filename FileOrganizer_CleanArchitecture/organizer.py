from scanner import scan_directory
from helper import print_files

class FileOrganizer:
    def __init__(self):
        self.path=r"H:\ISO\Project_testOnly"
        
        self.allFiles=[]

    def run(self):
        self.allFiles=scan_directory(self.path)
        print_files(self.allFiles)
