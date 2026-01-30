# Week03 Lab03 - Q4

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Charlie", "Diana", "Eve", "Frank"}

monday_class.add("Grace")
print(f"Monday Class: {monday_class}")
print(f"Wednesday Class: {wednesday_class}")
print(f"Both Classes: {monday_class & wednesday_class}") # Shift + 7
print(f"All Students: {monday_class | wednesday_class}")  # | = pipe, Shift +\
print(f"Students only in Monday Class: {monday_class - wednesday_class}")
print(f"Only in one of the classes: {monday_class ^ wednesday_class}")

all_students = monday_class | wednesday_class
print(f"Is Monday subset of all students:", monday_class <= all_students)
