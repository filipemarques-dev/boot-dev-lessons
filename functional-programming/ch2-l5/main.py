def change_bullet_style(document):
    lines_list = document.split("\n")
    # print(lines_list)
    new_document = map(convert_line, lines_list)
    rejoined_doc = "\n".join(list(new_document))
    # print(rejoined_doc)
    return rejoined_doc

# BOOT-DEV SOLUTION
def change_bullet_style2(document):
    return "\n".join(map(convert_line, document.split("\n")))
    

# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line