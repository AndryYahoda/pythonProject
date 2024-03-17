import My_data
from My_data import shawarma
from My_data import shawarma_description
from My_data import my_dict


def change():
    shawarma.remove('соус')
    shawarma.remove('капуста')
    shawarma.add('морква')
    shawarma.add("сметана")


def get_descript():
    print(shawarma_description)


def get_my_dict():
    print(my_dict)


print(my_dict)
print(type(shawarma))
print(shawarma_description)
print("склад до змін: " + str(shawarma))
change()
print("склад після змін: " + str(shawarma))
