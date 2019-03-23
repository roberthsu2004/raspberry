empty_dict = {}
print(empty_dict)
area_dict = {
    "tw":"Taiwan",
    "cn":"China",
    "hk":"Hong Kong"
    }
print(area_dict)
lol = dict([('a','b'), ('c','d')])
print(lol)

pythons = {
        "Chapman": "Graham",
        "Cleese": "John",
        "Idle": "Eric",
        "Jones": "Terry",
        "Palin": "Michael"
    }
print(pythons)
#insert
pythons["Gilliam"] = "Gerry"
print(pythons)
pythons["Gilliam"] = "Terry"
print(pythons)

others = {'Marx':'Groucho', 'Howard': "Moe"}
pythons.update(others)
print(pythons)

print("marx" in pythons)
print(pythons.get("marx"))
print(list(pythons.keys()));
print(list(pythons.values()));

for item in pythons.values():
    print(item);

for (key,value) in pythons.items():
    print(key,value)

birds = pythons.copy()

