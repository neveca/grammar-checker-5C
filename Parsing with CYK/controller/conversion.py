def conversion(raw):
    cnf = []
    for line in raw:
        cnf.append(line.split(' -> '))
    for rule in cnf:
        rule[1] = set(rule[1].split(' | '))
    for rule in cnf:
        temp = set()
        for element in rule[1]:
            element_to_tuple = tuple(element.split(' '))
            temp.add(element_to_tuple)
        rule[1] = temp
    print("Conversion done")
    return cnf
