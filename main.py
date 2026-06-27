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

        self.FolderNaming = ["PDF_Files","Image_Files","MP3_Files","ZIP_Files","EXE_Files",
                             "Excel_Files","Text_Files","UnityPacages","Text_Files","User_Folders"]


    #program flow manager
    def run(self):
        #self.get_directory()
        self.print_directory()
        self.scan_userDirectory()
        self.categorize_Files()
        self.print_allcategory()


    #function to get directory details from user
    def get_directory(self):
        self.userDirectory=input()

    #scan all files in that directory
    def scan_userDirectory(self):
        self.allFiles = os.listdir(self.userDirectory)
        

    def categorize_Files(self):
        for current_file in self.allFiles:
            if(current_file[-3::] =="pdf"):
                self.pdfFiles.append(current_file)
            elif(current_file[-3::]=="png"):
                self.imageFiles.append(current_file)
            elif(current_file[-3::]=="jpg"):
                self.imageFiles.append(current_file)
            elif(current_file[-3::]=="zip"):
                self.zipFiles.append(current_file)
            elif(current_file[-3::]=="txt"):
                self.txtFiles.append(current_file)
            elif(current_file[-3::]=="mp3"):
                self.mp3Files.append(current_file)
            elif(current_file[-3::]=="exe"):
                self.exeFiles.append(current_file)
            elif(current_file[-4::]=="xlsx"):
                self.xlsxFiles.append(current_file)
            elif(current_file[-12::]=="unitypackage"):
                self.unitypackage.append(current_file)
            
            #for folder categorizing
            else:
                #ignoring already creaded folder
                if(current_file in self.FolderNaming):
                    pass
                #if not our folder then catogorize it
                else:
                    self.Folders.append(current_file)
                    
            


        

    def create_Folders(self):
        #custom folder naming:
        '''
        pdf fies = PDF_Files
        
        '''
        pass

    def move_FilesToFolders(self):
        pass

    #test functions
    def print_directory(self):
        print(self.userDirectory)
    def print_allcategory(self):
        print("--------folders--------")
        print(self.Folders)
        print("--------images--------")
        print(self.imageFiles)
        print("--------pdfs--------")
        print(self.pdfFiles)
        print("--------exeFiles--------")
        print(self.exeFiles)
        print("--------zipfies--------")
        print(self.zipFiles)
        print("--------Excelfiles--------")
        print(self.xlsxFiles)
        print("--------UnityPackages--------")
        print(self.unitypackage)
        print("--------mp3 Files--------")
        print(self.mp3Files)
        print("--------text files--------")
        print(self.txtFiles)








    
    


if __name__=="__main__":
    organizer= FileOrganizer()
    organizer.run()
