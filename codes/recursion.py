# Font: https://realpython.com/python-recursion/

#Traverse a Nested List Recursively

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

print(len(names))

for index, item in enumerate(names):
    print(index, item)

def count_leaf_items(item_list):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    print(f"List: {item_list}")

    count = 0

    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items(item)
        else:
            print(f"Counted leaf item \"{item}\"")
            count += 1

    print(f"-> Returning count {count}")
    return count
