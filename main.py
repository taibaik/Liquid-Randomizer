import random

liquid = ['Fla and furious Raisin flurry', 'Oat drip V5', 'Es krim mall Platinum Vape', 'Bon dan bolu pandan', 'Milk zhake', 'Hokkaido cheese tart', 'Cracks Strawberry cheese', 'The black Forest', 'Krusty crepes v1', 'English breakfast v3', 'Mango Candy', 'Caramel Popcorn', 'Oat drips (cereal Milk','Dark Luna Masterpiece (Graham Cheesecake Strawberry)', 'Americak Breakfast (Strawberry Cereal Oats','Licky Drip (Red Velvet Cookised & Cream)','Tokyonarilla Premium Pod Liquid','Creamy Kopi Tiramisu','Solace Creamy Tobacco','Jasuke Caramel Creamy','Mix Fruit Candy Creamy','Bukan Liquid KW(Strawberry Biscuit Pudding','Liquid Cream Raisin (Rum Raisin Ice Cream','Juice Nation Ala Carte Cream Pound Cake','Strawbacco (Strawberry Tobacco)']
for x in range(3):
    chosen_liquid=liquid[random.randint(0,len(liquid)-1)]
    liquid.remove(chosen_liquid)
    print(chosen_liquid)
