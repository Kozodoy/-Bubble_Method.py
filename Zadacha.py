print("Hey, what`s up?")
data = open("file.txt", "r")
loop = data.readlines()
for line in loop:
    List = line.split(" ")
    print(List)

for i in range(0, len(List)):
    for k in range(i+1, len(List)):
        if List[i] > List[k]:
            c = List[i]
            List[i] = List[k]
            List[k] = c
        else:
            pass
print(List)





