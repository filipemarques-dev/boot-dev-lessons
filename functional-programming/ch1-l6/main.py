def get_median_font_size(font_sizes):
    
    list_length = len(font_sizes)
    sorted_list = sorted(font_sizes)
    
    print(sorted_list)
    
    if list_length % 2 != 0:
        return sorted_list[list_length // 2]
        
    if len(font_sizes) == 0:
        return None

    return sorted_list[(list_length // 2) -1]

#BOOT-DEV SOLUTION
def get_median_font_size_2(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]