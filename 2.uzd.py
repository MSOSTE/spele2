user_input = str(input("Ievadi skaitli: "))
i = 1
for i in range(int(user_input)):
    i = i + 1
    atlikums = user_input % i
    atlikums = int(atlikums)
    if atlikums > 0:
        print("Tas ir pirmskaitlis:(")
    else:
        print("Tas nav pirmskaitlis!")
