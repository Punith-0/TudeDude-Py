def main() -> None:
    students = {
        "student 1": {"Name": "Alice", "Age": 15, "Marks": 85},
        "student 2": {"Name": "John", "Age": 14, "Marks": 87},
        "student 3": {"Name": "Carol", "Age": 16, "Marks": 15}
    }

    name = input("Enter student name: ").strip()

    found = False
    for student, info in students.items():
        if info["Name"].lower() == name.lower():
            print(f"Marks of {info['Name']}: {info['Marks']}")
            found = True
            break

    if not found:
        print("Student not found in the dictionary.")


main()
