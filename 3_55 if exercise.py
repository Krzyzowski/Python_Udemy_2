
experience = 2
languages =["python", "typescript", "javascript", "java"]
print(type(languages))
print(languages)
contractType = "employment"

if experience >= 2 and (("python" and "java") in languages):
    if contractType == "b2b" or contractType == "employment":
        print("hired")
    else:
        print("Pracownik nie spełnia wymogu typu zatrudnienia: ", contractType)

else:
    print("not hired")