
abc = "abcdefghijklmnñopqrstuvwxyz"

def cifradocesar (cad_orig, clv):

    cad_cifrada = ""

    if clv >= len(abc):
        clv = clv % len(abc)

    for i in cad_orig:
        if i in abc: 
            pos = (abc.index(i) + clv)
            cad_cifrada += abc[pos]
        else:
            cad_cifrada += i
    return cad_cifrada


mensaje = "hola me llamo jose"
clave = 5

mensajecifrado = cifradocesar (mensaje, clave)

print ({mensaje})
print ({mensajecifrado})