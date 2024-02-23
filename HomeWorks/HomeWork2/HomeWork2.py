#My first favorite dish

shawarma = {'лаваш','м ясо','картопля','огірок','капуста','соус'}
shawarma_description = 'На смак як шаурма'

#My second favorite dish
burger = {'булочка','котлета','листя салату','огірок','соус','сир'}
burger_description = 'На смак як бургер'



#My third favorite dish
dumplings = {'тісто','фарш','цибуля','сіль','перець (чорний)'}
dumplings_description = 'на смак як пельмені'


my_dict = {
    'лаваш': 1,
    'м ясо (г)': 200,
    'картопля': 1,
    'огірок': 1,
    'капуста': 1,
    'соус (г)': 75,
    'булочка': 1,
    'котлета': 1,
    'листя салату': 2,
    'огірок (г)': 1,
    'сир (г)': 2,
    'тісто (кг)': 1,
    'фарш (г)': 700,
    'цибуля': 2,
    'сіль (г)': 15,
    'перець(чорний)(г)': 5,
}
print(my_dict)
print(type(shawarma))
print(type(burger))
print(type(dumplings))
print(shawarma_description)
print(burger_description)
print(dumplings_description)
print("склад до змін: " + str(shawarma))
shawarma.remove('соус')
shawarma.remove('капуста')
shawarma.add('морква')
shawarma.add("сметана")
print("склад після змін: " + str(shawarma))