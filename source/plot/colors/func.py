def get_colors(src):
    colors=[]
    f = open(src, 'r')
    for line in f.readlines():
        colors.append(line.strip())
    f.close()
    return colors