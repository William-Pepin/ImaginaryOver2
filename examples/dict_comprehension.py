identificators = ["1F", "2C", "3B", "4D", "5G"]
names = ["Steve", "Stephen", "Sarah", "Bob", "Alice"]

id_to_name = {id: name for id, name in zip(identificators, names)}

print(id_to_name["1F"])
