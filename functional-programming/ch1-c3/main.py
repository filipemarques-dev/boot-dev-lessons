def deduplicate_lists(lst1, lst2, reverse=False):
    combined_lst = lst1 + lst2
    remove_duplicates = set(combined_lst)
    result = sorted(remove_duplicates, reverse=reverse)
    return result

#BOOT-DEV SOLUTION
def deduplicate_lists2(lst1, lst2, reverse=False):
    return sorted(set(lst1 + lst2), reverse=reverse)