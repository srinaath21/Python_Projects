def full_name(fname : str, lname : str):
    fname = fname.capitalize()
    lname = lname.capitalize()
    return fname+" "+lname

firstname = input("Enter your first name:") 
lastname = input("Enter your last name:")
output = full_name(firstname, lastname)
print(f"Your full name is {output}")