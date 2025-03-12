def file_type_getter(file_extension_tuples):
    ext_dict = {}
    for file_type, ext_list in file_extension_tuples:
        # print(f"file type: {file_type}  |  extensions: {ext_list}")
        for extension in ext_list:
            # print(extension)
            ext_dict[extension] = file_type
    # print(ext_dict)
    get_file_ext = lambda extension: ext_dict.get(extension, "Unknown")
    return get_file_ext

# BOOT-DEV SOLUTION
def file_type_getter2(file_extension_tuples):
    file_extensions_dict = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extensions_dict[ext] = tup[0]
    return lambda ext: file_extensions_dict.get(ext, "Unknown")
