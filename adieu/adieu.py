import inflect

p = inflect.engine()

names_list = []r
while True:
    try:t
        name = input("Name: ")
        names_list.append(name)
    except EOFError:p
        print()
        breake
output = p.join(names_list)
print("Adieu, adieu, to "+ output)
