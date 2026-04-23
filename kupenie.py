ciel = int(input("zadaj ciel: "))
prijem = int(input("zadaj prijem: "))
mam = int(input("zadaj kolko máš: "))
mesiace = (ciel - mam) / prijem
print(f"Potrebuješ {ciel - mam} aby si dosiahol svoj ciel")
print(f"ak budeš mať {prijem} každý mesiac, tak ti bude trvať {mesiace} mesiacov aby si dosiahol svoj ciel")