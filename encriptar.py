abc = list("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890")

def cifrado_cesar(cad_original, clv):

    cad_cifrada = ""  # Cadena para almacenar el mensaje cifrado

    # Aseguramos que la clave esté dentro de los límites del abecedario
    if clv >= len(abc):
        clv = clv % len(abc)

    # Cifrar cada letra del mensaje
    for i in cad_original:
        if i in abc:  # Solo ciframos si el caracter está en el abecedario
            pos = (abc.index(i) + clv) % len(abc)  # Desplazamos la posición y nos aseguramos de que esté dentro de los límites
            cad_cifrada += abc[pos]
        else:
            cad_cifrada += i  # Si el carácter no está en el abecedario, lo agregamos tal cual (por ejemplo, espacios y puntuación)

    return cad_cifrada

# Ejemplo de uso:
mensaje = "jajajaja"
clave = 7  # La clave es el número de desplazamientos

mensaje_cifrado = cifrado_cesar(mensaje, clave)
print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {mensaje_cifrado}")


def descifrado_cesar(mensaje_cifrado, clv):
    cad_descifrada = ""
    
    if clv >= len(abc):
        clv = clv % len(abc)

    for i in mensaje_cifrado:
        if i in abc:
            pos = (abc.index(i) - clv)  # Desplazamos hacia atrás
            cad_descifrada += abc[pos]
        else:
            cad_descifrada += i  # Si el carácter no está en el abecedario (como los espacios), lo dejamos igual
    return cad_descifrada


descifrado = descifrado_cesar (mensaje_cifrado, clave)
print ({descifrado})

def fuerza_bruta_cesar(cad_cifrada):
    # Probamos todas las claves posibles (de 0 a 25)
    for clv in range(26):  # 26 es el tamaño del alfabeto en este caso
        mensaje_descifrado = descifrado_cesar(cad_cifrada, clv)
        print(f"Clave: {clv} -> Mensaje descifrado: {mensaje_descifrado}")

fuerza_bruta_cesar (mensaje_cifrado)