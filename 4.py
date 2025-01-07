# MI RESPUESTA, 5 ESTRELLAS
def create_xmas_tree(height, ornament):
    # Code here
    tree = ""
    for i in range(height)[::-1]:
        tree += i * '_'
        tree += ornament * (1+((height-i-1)*2))
        tree += i * '_'
        tree += "\n"
    foot = '_' * (height-1) + '#' + '_' * (height-1) + '\n'
    tree += foot * 2
    return tree