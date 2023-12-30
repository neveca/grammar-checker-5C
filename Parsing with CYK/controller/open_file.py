#Digunakan untuk membuka aturan CNF dan mengembalikannya dalam suatu list 
def open_file(filepath):
    rules = []
    with open(filepath, 'r') as file:
        raw = file.readlines()
        for data in raw:
            rules.append(data.strip('\n'))
    return rules