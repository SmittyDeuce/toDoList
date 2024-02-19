toDo = []
errands = input("what all do you have to do today? (press Enter if none)")

if errands != "":
    toDo.append(errands)
anythingElse = input("anything else? (press Enter if none)")
while anythingElse != '':
    toDo.append(anythingElse)
    anythingElse = input("anything else? (press Enter if none)")
else:
    print("why are you even here go relax and enjoy your day")


print(toDo)