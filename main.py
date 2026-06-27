import os
import shutil
class FileOrganizer:

    

    def __init__(self):
        self.userDirectory= r"H:\ISO\Project_testOnly"
        self.allFiles=[]

        #Different file Types
        self.pdfFiles=[]
        self.imageFiles=[] #png, jpg,jpeg
        self.mp3Files=[]
        self.zipFiles=[]
        self.exeFiles=[]
        self.xlsxFiles=[]
        
        self.txtFiles=[]
        self.unitypackage=[]
        
        self.Folders=[]

        self.FolderNaming = ["PDF_Files","Image_Files","MP3_Files","ZIP_Files","EXE_Files",
                             "Excel_Files","UnityPackages","Text_Files","User_Folders"]


    #program flow manager
    def run(self):
        #self.get_directory()
        self.print_directory()
        self.scan_userDirectory()
        self.categorize_Files()
        #self.print_allcategory()
        self.create_Folders()
        self.move_FilesToFolders()
        self.move_FolderstoFolders()


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
                full_path = os.path.join(self.userDirectory, current_file)

                if os.path.isdir(full_path):
                    if current_file not in self.FolderNaming:
                        self.Folders.append(current_file)
                    

    def create_Folders(self):
        #creating folders based on the Folder_naming list

        for folderName in self.FolderNaming:
            if(folderName not in self.allFiles):
                final_folder_path = os.path.join(self.userDirectory,folderName)
                os.mkdir(final_folder_path)

    def move_FilesToFolders(self):
        #move pdf files
        for pdf in self.pdfFiles:
            source_path = os.path.join(self.userDirectory,pdf)
            destination_path = os.path.join(self.userDirectory,"PDF_Files")
            shutil.move(source_path,destination_path)
        #move image files
        for image in self.imageFiles:
            source_path = os.path.join(self.userDirectory,image)
            destination_path = os.path.join(self.userDirectory,"Image_Files")
            shutil.move(source_path,destination_path)
        
        #move MP3_Files
        for mp3 in self.mp3Files:
            source_path = os.path.join(self.userDirectory,mp3)
            destination_path = os.path.join(self.userDirectory,"MP3_Files")
            shutil.move(source_path,destination_path)


        #move ZIP_Files
        for zip in self.zipFiles:
            source_path = os.path.join(self.userDirectory,zip)
            destination_path = os.path.join(self.userDirectory,"ZIP_Files")
            shutil.move(source_path,destination_path)

        #move EXE_Files
        for exe in self.exeFiles:
            source_path = os.path.join(self.userDirectory,exe)
            destination_path = os.path.join(self.userDirectory,"EXE_Files")
            shutil.move(source_path,destination_path)

        #move Excel_Files
        for excel in self.xlsxFiles:
            source_path = os.path.join(self.userDirectory,excel)
            destination_path = os.path.join(self.userDirectory,"Excel_Files")
            shutil.move(source_path,destination_path)

        #move UnityPacages
        for unityPack in self.unitypackage:
            source_path = os.path.join(self.userDirectory,unityPack)
            destination_path = os.path.join(self.userDirectory,"UnityPackages")
            shutil.move(source_path,destination_path)

        #move Text_Files
        for text in self.txtFiles:
            source_path = os.path.join(self.userDirectory,text)
            destination_path = os.path.join(self.userDirectory,"Text_Files")
            shutil.move(source_path,destination_path)

    def move_FolderstoFolders(self):
        #move User_Folders
        for folder in self.Folders:
            source_path = os.path.join(self.userDirectory,folder)
            destination_path = os.path.join(self.userDirectory,"User_Folders")
            shutil.move(source_path,destination_path)

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
