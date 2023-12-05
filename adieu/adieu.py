import inflect

namelist = []

while True:
    try:
        name = input("Name: ")
        namelist.append(name)

    except EOFError:
        result = inflect.engine().join(namelist)
        print("")
        print("Adieu, adieu, to " + result)
        break
    else:
        continue
