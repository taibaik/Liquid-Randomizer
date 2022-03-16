import random

liquid = ['Fla and furious Raisin flurry', 'Oat drip V5', 'Es krim mall Platinum Vape', 'Bon dan bolu pandan', 'Milk zhake', 'Hokkaido cheese tart', 'Cracks Strawberry cheese', 'The black Forest', 'Krusty crepes v1', 'English breakfast v3', 'Mango Candy', 'Caramel Popcorn']
for x in range(3):
    chosen_liquid=liquid[random.randint(0,len(liquid)-1)]
    liquid.remove(chosen_liquid)
    print(chosen_liquid)