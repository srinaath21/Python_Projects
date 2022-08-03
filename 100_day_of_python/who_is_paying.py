import random

CSVnames = input("Enter the names: ")
names = CSVnames.split(", ")

end = len(names)

person_chosen = random.choice(names)
print(f"{person_chosen} has to pay the bill")