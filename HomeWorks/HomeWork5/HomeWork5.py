# Task 1
# text = "Hello! My name Andrew"
#
#
# def process_text(abc):
#     return abc
#
#
# print(process_text(text))

# Task 2
# text = "Hello! My name Andrew"
#
#
# def process_text(reverse=False):
#     if reverse == True:
#         print(text[::-1])
#     else:
#         print(text)
#
#
# process_text(True)
#
#
# process_text()
# Task 3
# text = "Hello! My name Andrew."
# args = ["And", "I'm", "12", "years", "old"]
#
#
# def process_text(*list):
#
#     global text
#     for item in list:
#         text = text + " " + item
#     return text
#
#
# print(process_text(*args))
# Task 4
# text = "Hello! My name Andrew"
# str1 = ""
# args = [" And", "I'm", "12", "years", "old"]
# kwargs = {"separator": "!!!",
#           "islower": True}
#
#
# def process_text(*list, **dict):
#     global text
#     global str1
#     for item in list:
#         str1 = str1 + " " + item
#     text = text + dict["separator"] + str1
#     return text


print(process_text(*args, **kwargs))
