with open('player_input_1', 'r') as file:
    txt = file.read(10)
    txt_splited = txt.split()
    awg = 0
    i = 1
    for word in txt_splited:
        awg = (awg + len(word))/ i
        i += 1
    print(awg)
