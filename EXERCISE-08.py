names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Enter the name you want to search for: ")

if search_name in names:
    print(search_name, "was found in the list.")
else:
    print(search_name, "was not found in the list.")
