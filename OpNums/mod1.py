def MaxNum(n1, n2):
    if n1 > n2:
        print("O Primeiro número é maior que o 2º")
    else:
        print("O Segundo número é maior que o 1º")

    return


n1 = int(input(f"Insira o Primeiro Valor"))
n2 = int(input(f"Insira o Segundo Valor"))


def numLen(number):
    n = str(number)
    if len(n) > 1:
        if a[0] == '0':
            return len(n) - 1
        else:
            return len(n)
    return len(n)


number = int(input(f"Insira o Número"))
numLen(number)
