f = open("my_first_file.txt", "w", encoding='utf-8')
f.write('Новий рядок який ми записали')
f = open("my_first_file.txt", "r", encoding='utf-8')
print(f.read())
