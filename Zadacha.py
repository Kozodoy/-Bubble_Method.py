print("Hey, what`s up?")
List = [5, 4, 3, 8, 9, 10]
for i in range(0, len(List)):
    for k in range(i+1, len(List)):
        if List[i] > List[k]:
            c = List[i]
            List[i] = List[k]
            List[k] = c
        else:
            pass
print(List)





