player_input = input("Введіть текст який ви бажаєте: ")
with open('player_input_1', 'w') as file:
    file.write(player_input)
with open('player_input_1', 'r') as file:
    txt = file.read()
    txt_splited = txt.split()
    print(len(txt_splited))


