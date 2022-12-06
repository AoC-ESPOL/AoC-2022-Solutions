with open("day_06.txt") as file:
    contenido = file.read()
def buscador(tamaño):
    for i in range(len(contenido)-tamaño):
        sin_repetir = set(contenido[i:i+tamaño])
        if len(sin_repetir) == tamaño:
            return i + tamaño

print("Respuesta1:", buscador(4))
print("Respuesta2:", buscador(14))

