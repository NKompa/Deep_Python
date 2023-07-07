def split_link(link):
    path, filename = link.rsplit('\\', 1)
    filename, extension = filename.split('.', 1)
    return path, filename, extension


link1 = "D:\Documents\English\Words\Words_List.xlsx"
print(split_link(link1))