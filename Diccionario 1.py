None
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL":"una respuesta a una broma",
            "SHEESH":"ligera desaprobación",
            "CREEPY ":"aterrador, siniestro",
            "AGGRO":"ponerse agresivo/enojado"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No se tiene esa  palabra en el dicionario, por favor pruebe con otra palabra")
