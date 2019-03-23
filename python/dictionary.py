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
#https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/raspberry-pi-3-model-b-%E8%88%87-hc-sr04-%E8%B6%85%E9%9F%B3%E6%B3%A2%E6%84%9F%E6%B8%AC%E5%99%A8%E4%B9%8B%E6%87%89%E7%94%A8
#https://github.com/alaudet/hcsr04sensor
