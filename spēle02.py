text = input("Ievadi tekstu: ")
tt = list(text)
t2 = ""
for simb in tt:
    if simb == " ":
        t2 += " "
    else:
        t2 += "*"
print(t2)
t2 = str(t2)

while "*" in t2:
    gg = input("Atmini burtu: ")
    start = 0
    index1 = []
    t = text.count(gg)
    for i in range(t):
        index = text[start:].find(gg)
        if index != -1:
            index1.append(start + index)
        start += index + 1
    t2 = list(t2)
    for index in index1:
        t2[index] = gg
    text = "".join(t2)
    print(text)
