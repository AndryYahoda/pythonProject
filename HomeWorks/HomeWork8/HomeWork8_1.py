# Task 3
import random
number_of_symbols = int(input("Enter number of symbols for generation: "))
i = 0
result = []
all_symbols = 'ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstvxyz1234567890'
for i in range(number_of_symbols):
    symbol = random.choice(all_symbols)
    result.append(symbol)
result_as_string = ''.join(result)
print(result_as_string)






