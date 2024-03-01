"""
 sum vid 1 do 100
 a = 1 + 2 + 3 + 4 + 5 + 6

 range(1,6)
 1, 2, 3, 4, 5

 range(1, 101)
 [1, 100)
 1, 2, 3, 4, 5 ... 99, 100

 result = 0
 for i in range(0, 101, 2):
   result += i

 print(result)

 result_1 = 0
 for i in range(5):
   print(i)


for i in range(0, 101, 2):
    print(i)

range(5)
range(0, 5)
range(1, 101, 2)

list = ['apple', 'orange', 'potato']
for element in list:
    print(element)


i = 0

i = i + 1
i += 1
i -= 1
"""

i = 1
sum = 0
while i < 6:
    sum += i
    i += 1

print(sum)
