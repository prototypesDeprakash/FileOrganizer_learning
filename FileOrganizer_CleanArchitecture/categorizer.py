import os

def categorize_Files(files_list,directory):
    files_category ={}
    for file in files_list:
        full_path = os.path.join(directory, file)
        if not os.path.isfile(full_path):
            continue
        
        name, ext = os.path.splitext(file)
        ext = ext.lower().lstrip(".")
        if ext:
            files_category.setdefault(ext, []).append(file)

        # if ext in files_category:
        #     files_category[ext].append(file)
        # else:
        #     files_category[ext]=[file]
    return files_category