def create_summary(category_dictionary, created_folders):
    finalresult=[]
    total_items = 0

    finalresult.append("\n" + "=" * 60)
    finalresult.append("                 FILE ORGANIZER SUMMARY")
    finalresult.append("=" * 60)

    finalresult.append("\nFolders Created")
    finalresult.append("-" * 60)

    if created_folders:
        for folder in created_folders:
            finalresult.append(folder)
    else:
        finalresult.append("No new folders created.")

    finalresult.append("\nFiles Moved")
    finalresult.append("-" * 60)

    for key in category_dictionary:

        if key == "All_Folders":
            folder_name = "User_Folders"
        else:
            folder_name = key.capitalize() + "_Files"

        finalresult.append(f"\n{folder_name}")
        finalresult.append("-" * len(folder_name))

        for file in category_dictionary[key]:
            finalresult.append(f"  {file}")

        finalresult.append(f"\nItems moved : {len(category_dictionary[key])}")

        total_items += len(category_dictionary[key])

    finalresult.append("\n" + "=" * 60)
    finalresult.append(f"Total Items Moved : {total_items}")
    finalresult.append(f"Folders Created   : {len(created_folders)}")
    finalresult.append("=" * 60)
    print(finalresult)
    return finalresult