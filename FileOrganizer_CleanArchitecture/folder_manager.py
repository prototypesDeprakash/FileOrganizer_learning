import os 
def create_folders(extention_list,directory):
    folder_name_list=[]
    folderName = ""
    for ext in extention_list:
        folderName = str(ext.capitalize()+"_Files")
        folder_name_list.append(folderName)
        
        final_folder_path = os.path.join(directory,folderName)
        if not os.path.exists(final_folder_path):
            os.mkdir(final_folder_path)
    return folder_name_list
        

 
                
                


