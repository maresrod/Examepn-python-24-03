'''
Autor: Marcelo Espinola Rodriguez
Version de python: 3.9
'''


def get_list(nombre_fichero):
    f = open(nombre_fichero, mode="r", encoding="utf-8")
    texto = f.read()
    if texto == "":
        raise ValueError("El archivo esta vacio")
    else:
        parsed_text = texto.split()

        final_list = []
        max_len = 0
        for word in parsed_text:
            if word not in final_list:
                if len(word) > max_len:
                    max_len = len(word)
                final_list.append(word)
        print(final_list)
        print(max_len)

        keys = range(1, max_len+1)

        diccionario ={k: [] for k in keys}
        print(diccionario)



get_list("texto.txt")
