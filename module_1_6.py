# Работа со словарями

my_dict = {"Pizza": 922479, "Dog": 1988, "Year": 2024}
print(my_dict)
print(my_dict["Pizza"])
print(my_dict.get("Name"))
my_dict["David"] = 2006
my_dict["Weight"] = 50
a = my_dict.pop("Dog")
print(a)
print(my_dict)

# Работа с множествами

my_seat = {41, 2002, False, 25, "Work", 2002, "Work", True, 41, True, "Good", 25}
print(my_seat)
my_seat.add(1000)
my_seat.add(19.20)
my_seat.discard(2002)
print(my_seat)