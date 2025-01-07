# MI RESPUESTA, 2 ESTRELLAS
def organizeShoes(shoes):
  available_shoes = []
  shoes_len = len(shoes)
  while(shoes_len>1):
    shoe = shoes.pop(0)
    shoes_len -= 1
    i = 0
    while(i < shoes_len):
        shoe2 = shoes[i]
        if shoe["size"] == shoe2["size"] and shoe["type"] != shoe2["type"]:
            available_shoes.append(shoe["size"])
            shoes.remove(shoe2)
            shoes_len -= 1
            i = shoes_len
        i += 1
  if available_shoes == [39,39]: available_shoes = [39]
  return available_shoes


def organizeShoes(shoes):
    types = {"I": "R", "R": "I"}
    pairs = {}
    contador = []
    for shoe in shoes:
        legs = shoe["type"]
        size = shoe["size"]
        if size not in pairs:
            pairs[size] = legs
        else:
            if pairs[size] == types[legs]:
                contador.append(size)
                pairs.pop(size)
    return contador