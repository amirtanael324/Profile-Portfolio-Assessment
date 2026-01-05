names = ["jake", "zac", "ian", "ron", "sam", "dave"]
search_name = input("Enter the name to search for: ")
found = False
for name in names:
    if name == search_name.lower():
        found = True
        break
if found:
    print(f"{search_name} found in the list.")
else:
    print(f"{search_name} not found in the list.")
