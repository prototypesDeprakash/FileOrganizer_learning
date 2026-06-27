import os

def scan_directory(path):
    return os.listdir(path)


def get_file_extensions(files_list, directory):
    extension_list = set()
    for file in files_list:
        full_path = os.path.join(directory, file)
        if not os.path.isfile(full_path):
            continue
        name, ext = os.path.splitext(file)
        if ext:
            extension_list.add(ext.lower().lstrip("."))
    return list(extension_list)

