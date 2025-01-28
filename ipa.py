def convertir_nombres(texto):
    import re
    # Remover números y comas asociadas
    t = re.sub(r'\d+(\,\d+)*', '', texto)
    # Remover la palabra 'and' si está presente
    t = t.replace('and ', '')
    # Dividir la cadena en nombres individuales
    ns = t.split(', ')
    # Convertir cada nombre
    ns_convertidos = []
    for n0 in ns:
        partes = n0.strip().split()
        ln = partes[-1]
        n0 = ' '.join(partes[:-1])
        ns_convertidos.append(f"{ln}, {n0}")
    # Unir todos los nombres convertidos con '; '
    resultado = '; '.join(ns_convertidos)
    return resultado

texto = input()
resultado = convertir_nombres(texto)
print(resultado)
