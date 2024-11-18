# Работа со словарями
my_dict = {"Dmitriy": 1995, "Ivan": 2000, "Alex": 1991}
print("Dict: ", my_dict)
print("Existing value: ", my_dict.get("Dmitriy"))
print("Not existing value: ", my_dict.get("Vladimir"))
my_dict["Vladimir"] = 1999
print("Added value: ", my_dict["Vladimir"])
my_dict.update({"Anna": 2003,
                "Natalia": 1990})
deleted_list = my_dict.pop("Alex")
print("Removed value: ",deleted_list)
print("Modified dictionary: ", my_dict)
print()
# Работа с множествами
my_set = {4, 4, 8, 8, 8, 23, 42, 42, "lost", "lost", True}
print("Set: ", my_set)
my_set.update([15, 16])
my_set.discard(True)
print("Modified set: ", my_set)
print()
# Сортировка для красоты
my_set.discard("lost")
sorted = sorted(my_set)
print("Sorted set: ", sorted)
