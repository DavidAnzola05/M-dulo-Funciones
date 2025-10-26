def es_palindromo_DAAC(palabra_DAAC):
    p = palabra_DAAC.lower().replace(" ", "")
    return p == p[::-1]

print(es_palindromo_DAAC("anita lava la tina"))
