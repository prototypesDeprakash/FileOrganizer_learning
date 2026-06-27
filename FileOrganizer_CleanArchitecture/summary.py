def create_summary(category_dictionary, created_folders):
    total_items = 0

    print("\n" + "=" * 60)
    print("                 FILE ORGANIZER SUMMARY")
    print("=" * 60)

    print("\nFolders Created")
    print("-" * 60)

    if created_folders:
        for folder in created_folders:
            print(folder)
    else:
        print("No new folders created.")

    print("\nFiles Moved")
    print("-" * 60)

    for key in category_dictionary:

        if key == "All_Folders":
            folder_name = "User_Folders"
        else:
            folder_name = key.capitalize() + "_Files"

        print(f"\n{folder_name}")
        print("-" * len(folder_name))

        for file in category_dictionary[key]:
            print(f"  {file}")

        print(f"\nItems moved : {len(category_dictionary[key])}")

        total_items += len(category_dictionary[key])

    print("\n" + "=" * 60)
    print(f"Total Items Moved : {total_items}")
    print(f"Folders Created   : {len(created_folders)}")
    print("=" * 60)