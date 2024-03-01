filter = input('Введіть ваш запит (snidanok, obid, perekus1, perekus2, vechera): ')

if filter == 'obid':
    obid = 'Обід: м\'ясо, суп, шаурма'
    print(obid)
elif filter == 'perekus 1':
    perekus1 = 'Перекус 1: апельсин'
    print(perekus1)
elif filter == 'vecheria':
    vechera = 'Вечеря: омлет, кава, сік'
    print(vechera)
elif filter == 'perekus 2':
    perekus2 = 'Перекус 2: горішки'
    print(perekus2)
elif filter == 'snidanok':
    snidanok = 'Сніданок: Млиньці, ковбаса, кава'
    print(snidanok)
else:
    print('Введіть ща раз')
