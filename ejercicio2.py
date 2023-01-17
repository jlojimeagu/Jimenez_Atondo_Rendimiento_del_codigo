nif_dict = {'0': 'T', '1': 'R', '2': 'W', '3': 'A', '4': 'G', '5': 'M', '6': 'Y', '7': 'F', '8': 'P', '9': 'D',
            '10': 'X', '11': 'B', '12': 'N', '13': 'J', '14': 'Z', '15': 'S', '16': 'Q', '17': 'V', '18': 'H',
            '19': 'L', '20': 'C', '21': 'K', '22': 'E'}
def check_nif(nif):
    """
        :param nif: numero de identificacion
        :return: correccion del numero de identificacion
        """
    if nif == 'DNI':
        return nif
    else:
        dni = str(nif)
        num = dni[0:8]
        check = int(num) % 23
        good_num = nif_dict[str(check)]
    return num + good_num

def check_username(nombre, apellido):
    """
    :param nombre: el nombre de la persona
    :param apellido: el apellido o apellidos.
    :return:retorna su respectivo dato con la inicial en
    mayuscula
    """
    return nombre.title() + ' ' + apellido.title()

print(check_username("juan miguel","jimenez aguas"))