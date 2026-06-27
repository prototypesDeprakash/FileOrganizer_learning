import os

class FileOrganizer:

    

    def __init__(self):
        self.userDirectory="H:\ISO"
        self.allFiles=[]

        #Different file Types
        self.pdfFiles=[]
        self.imageFiles=[] #png, jpg,jpeg
        self.mp3Files=[]
        self.zipFiles=[]
        self.exeFiles=[]
        self.xlsxFiles=[]
        self.exeFiles=[]
        self.txtFiles=[]
        self.unitypackage=[]
        self.Folders=[]


    #program flow manager
    def run(self):
        #self.get_directory()
        self.print_directory()
        self.scan_userDirectory()


    #function to get directory details from user
    def get_directory(self):
        self.userDirectory=input()

    #scan all files in that directory
    def scan_userDirectory(self):
        self.allFiles = os.listdir(self.userDirectory)
        for i in self.allFiles:
            print(i)






    #test functions
    def print_directory(self):
        print(self.userDirectory)
    
    


if __name__=="__main__":
    organizer= FileOrganizer()
    organizer.run()
