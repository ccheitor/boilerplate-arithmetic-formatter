
def arithmetic_arranger(lista: list, controle:bool = False):
    
    def validador_parse(*args):
        _validator_error = False
        for operator in args:
            try:
                int(operator)
            except ValueError:
                _validator_error = True
        return _validator_error

    if len(lista)>5:
        return "Error: Too many problems."

    str_operator_1=''
    str_operator_2=''
    str_resul=''
    str_ifen=''

    for item in lista:
        _ = item.split()
        
        if _[1] not in ('+','-'):
            return "Error: Operator must be '+' or '-'."

        if validador_parse(_[0],_[2]):
            return "Error: Numbers must only contain digits."

        if (len(str(_[0]))>4 or len(str(_[2]))>4):
            return "Error: Numbers cannot be more than four digits."

        space_end = "    " if lista.index(item)<(len(lista)-1) else ""
        size = len(_[0]) if len(_[0])>=len(_[2]) else len(_[2])
        result = str(int(_[0])+int(_[2])) if _[1] == '+' else str(int(_[0])-int(_[2]))

        str_operator_1 += (' ' * (size - len(_[0])+2)) + _[0] + space_end
        str_operator_2 += _[1] + (' ' * ((size+1)  - len(_[2])))+ _[2] + space_end
        str_ifen += ('-' * (size+2)) + space_end
        str_resul += (' '* ((size+2) - len(result))) + result + space_end

    arranged_problems = str_operator_1 + '\n' + str_operator_2 + '\n'+ str_ifen + (('\n' + str_resul) if controle else '')

    return arranged_problems