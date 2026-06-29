import os 
def create_folders(extension_list, directory):
    folder_name_list = []

    # Create User_Folders
    user_folder = os.path.join(directory, "User_Folders")
    if not os.path.exists(user_folder):
        os.mkdir(user_folder)
        folder_name_list.append("User_Folders")

    # Create extension folders
    for ext in extension_list:
        folder_name = ext.capitalize() + "_Files"
        final_folder_path = os.path.join(directory, folder_name)

        if not os.path.exists(final_folder_path):
            os.mkdir(final_folder_path)
            folder_name_list.append(folder_name)

    return folder_name_list
                
                


