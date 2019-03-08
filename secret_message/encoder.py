import numpy

line = input("Tell me your secrets")
for char in line:
    if char in " ?.!/;:":
        line = line.replace(char,'')
line = line.lower()

print(line)

#make numbers larger than 26 into numbers less than 26
#because there are only 26 letters



#make a dictionary of values
dic = {"a":1,
       "b":2,
       "c":3,
       "d":4,
       "e":5,
       "f":6,
       "g":7,
       "h":8,
       "i":9,
       "j":10,
       "k":11,
       "l":12,
       "m":13,
       "n":14,
       "o":15,
       "p":16,
       "q":17,
       "r":18,
       "s":19,
       "t":20,
       "u":21,
       "v":22,
       "w":23,
       "x":24,
       "y":25,
       "z":26,
       }


output_message = [dic.get(n, n) for n in line]
print(output_message)

arrayed_message = numpy.array(output_message)
print(arrayed_message)
amount_of_shift = int(input("How many letters should we shift?"))
shifted_message = arrayed_message + amount_of_shift
print(shifted_message)
shifted_message[shifted_message>26]-=26
print(shifted_message)

reversedic = { 1:"a",
               2:"b",
               3:"c",
               4:"d",
               5:"e",
               6:"f",
               7:"g",
               8:"h",
               9:"i",
               10:"j",
               11:"k",
               12:"l",
               13:"m",
               14:"n",
               15:"o",
               16:"p",
               17:"q",
               18:"r",
               19:"s",
               20:"t",
               21:"u",
               22:"v",
               23:"w",
               24:"x",
               25:"y",
               26:"z"
               }

final_message = [reversedic.get(n, n) for n in shifted_message]
print(final_message)

