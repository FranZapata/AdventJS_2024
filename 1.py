# MI SOLUCION, 1 estrella
def prepare_gifts(gifts):
  # Code here
  ordered_gifts = []
  if len(gifts) > 0: ordered_gifts.append(gifts.pop(0))
  for gift in gifts:
    for i in range(len(ordered_gifts)):
        if gift < ordered_gifts[i]:
            ordered_gifts.insert(i,gift)
        elif gift == ordered_gifts[i]:
            break
    if gift > ordered_gifts[len(ordered_gifts)-1]:
        ordered_gifts.append(gift)
  return ordered_gifts


# SOLUCION MEJORADA, 2 estrellas
def prepare_giftsV2(gifts):
    resultado = []
    for num in gifts:
        if num not in resultado:
            resultado.append(num)
    
    # Ordenar manualmente
    for i in range(len(resultado)):
        for j in range(i + 1, len(resultado)):
            if resultado[i] > resultado[j]:
                # Intercambiar elementos
                resultado[i], resultado[j] = resultado[j], resultado[i]

    return resultado
