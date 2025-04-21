def list_files(parent_directory, current_filepath=""):
    filepath_lst = []
    for key in parent_directory:
        new_filepath = current_filepath + f"/{key}"
        if parent_directory[key] == None:
            filepath_lst.append(new_filepath)
        else:
            filepath_lst.extend(list_files(parent_directory[key], new_filepath))
    return filepath_lst