import shutil
import os


def move_files(all_folders_dictionary, directory):
    for ext in all_folders_dictionary:

        if ext == "All_Folders":
            folder_name = "User_Folders"
        else:
            folder_name = ext.capitalize() + "_Files"

        destination_path = os.path.join(directory, folder_name)

        # Create the folder if it doesn't exist
        os.makedirs(destination_path, exist_ok=True)

        for file in all_folders_dictionary[ext]:
            source_path = os.path.join(directory, file)
            shutil.move(source_path, destination_path)

'''

  for image in self.imageFiles:
            source_path = os.path.join(self.userDirectory,image)
            destination_path = os.path.join(self.userDirectory,"Image_Files")
            shutil.move(source_path,destination_path)
'''