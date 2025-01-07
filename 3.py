import json
# MI RESPUESTA, 4 ESTRELLAS
def organizeInventory(inventory):
    # Code here
    orgInventory = {}
    for article in inventory:
        if article["category"] in orgInventory:
            if article["name"] in orgInventory[article["category"]]:
                orgInventory[article["category"]][article["name"]] = orgInventory[article["category"]][article["name"]] + article["quantity"]
            else:
                orgInventory[article["category"]][article["name"]] = article["quantity"]
        else:
            orgInventory[article["category"]] = {
                article["name"] : article["quantity"]
            }
    return orgInventory


inventory = [
  { "name": 'doll', "quantity": 5, "category": 'toys' },
  { "name": 'car', "quantity": 3, "category": 'toys' },
  { "name": 'ball', "quantity": 2, "category": 'sports' },
  { "name": 'car', "quantity": 2, "category": 'toys' },
  { "name": 'racket', "quantity": 4, "category": 'sports' }
]

inventory2 = [
  { "name": 'book', "quantity": 10, "category": 'education' },
  { "name": 'book', "quantity": 5, "category": 'education' },
  { "name": 'paint', "quantity": 3, "category": 'art' }
]

print(json.dumps(organizeInventory(inventory), indent=4))

print(json.dumps(organizeInventory(inventory2), indent=4))