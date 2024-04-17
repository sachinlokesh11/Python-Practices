# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a
# dictionary of objects like { "name": "John", "top_note": 5 }.
# Examples
# top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
# top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
# top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }


def top_note(input_dict):
    all_notes = input_dict.get("notes")
    max_note = all_notes[0]
    for index in range(len(all_notes)-1):
        if all_notes[index+1] > all_notes[index]:
            max_note = all_notes[index+1]
    input_dict.update({"notes": max_note})
    input_dict["top_score"] = input_dict.pop("notes")
    return input_dict


if __name__ == "__main__":
    print(top_note({"name": "John", "notes": [3, 5, 4]}))
    print(top_note({ "name": "Max", "notes": [1, 4, 6]}))
    print(top_note({ "name": "Zygmund", "notes": [1, 2, 3]}))