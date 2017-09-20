def replaceAll(file, search_exp, replace_exp):
    for line in fileinput.input(file, inplace=1):
        if search_exp in line:
            line = line.replace(search_exp, replace_exp)
        sys.stdout.write(line)