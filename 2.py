
# MI RESPUESTA, 5 estrellas
def createFrame(names):
    # Buscamos el nombre mas largo
    max_length = 0
    str = ""

    for name in names:
        if len(name)>max_length: max_length = len(name)
    print(max_length)

    max_length += 4
    str += ('*' * (max_length)) + "\n"
    for name in names:
        str += f"* {name}{(' ' * (max_length - 3 - len(name)))}*\n"
    str += ('*' * (max_length))
    return str
