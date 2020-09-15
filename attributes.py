

def attribute_parser(string):
  string1 = string[1:len(string)-1]

  string2 = list(filter(lambda x:x != "", string1.split(":")))

  string3 = []

  string3.append([[], string2[0]])

  for thing in string2[1: len(string2)-1]:
    thing1 = thing.split(",")
    string3.append([thing1[:len(thing1)-1], thing1[len(thing1)-1]])

  string3.append([string2[len(string2)-1],[]])

  string4 = []

  for i in range(len(string3)-1):
    string4.append([string3[i][1], string3[i+1][0]])

  string5 = {}
  for thing in string4:
    string5[thing[0]] = ",".join(thing[1])

  return string5


print(attribute_parser("(Colors:blue, white,Special Note::very nice,Style: Modern)"))

