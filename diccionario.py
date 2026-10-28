word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "XD": "Una respuesta común a algo gracioso",
            "AURA": "tener mucho estilo",
            "CHILL": "de broma"
}

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("palabra desconocida")
