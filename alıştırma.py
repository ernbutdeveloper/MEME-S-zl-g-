meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "Olaganustu hareketlere karsilik",
            "TO AGGRO": "agresifleşmek/sinirlenmek"
            }
            
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_sozlugu.keys():
    print("Kelime sozlukte var")
    
else:
    print("Kelime sozlukte yok :(")
