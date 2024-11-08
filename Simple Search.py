names_list = ["Jake", "Zac", "Ian", "Sam", "Dave"]
search = input("Enter the name you want to search for: ")
if search in names_list:
    print(f"{search} is in the list")
else:
    print("Entered name not found on the list")
    