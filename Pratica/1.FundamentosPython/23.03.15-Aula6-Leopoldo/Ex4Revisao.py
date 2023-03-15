def frequenciaLetras (s):
    d ={}
    c = set(s)
    for letra in c:
        freq = s.count(letra)
        d[letra] = freq
    return d

print(frequenciaLetras("leopoldo"))