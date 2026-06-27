import os

def categorize_Files(files_list,directory):
    files_category ={}
    for file in files_list:
        full_path = os.path.join(directory, file)

        #folder
        if os.path.isdir(full_path):

            #ignore folders created by this program
            if file.endswith("_Files") or file == "User_Folders":
                continue

            files_category.setdefault("All_Folders",[]).append(file)
            continue

        #file
        name, ext = os.path.splitext(file)
        ext = ext.lower().lstrip(".")

        if ext:
            files_category.setdefault(ext, []).append(file)

        # if ext in files_category:
        #     files_category[ext].append(file)
        # else:
        #     files_category[ext]=[file]
    return files_category