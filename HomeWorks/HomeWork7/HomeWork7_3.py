def read_from_file_1():
    with open('player_input_1', 'r') as file:
        txt = file.read()
        txt_splited = txt.split()
        return len(txt_splited)


def read_from_file_2():
    with open('player_input_2', 'r') as file:
        txt2 = file.read()
        txt_splited2 = txt2.split()
        return len(txt_splited2)

if read_from_file_1() > read_from_file_2():
    print('There are more words in first file')
elif read_from_file_1() < read_from_file_2():
    print('There are more words in second file')
else:
    print('Count of words equals')
